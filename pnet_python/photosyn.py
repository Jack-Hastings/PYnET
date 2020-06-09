from math import pow, log10
from pnet_input import clim, share, site, veg


def photosyn(clim, share, site, veg, rstep):
    '''Photosynthesis routine for the PnET model'''

    psn_t_max = veg['psn_t_opt'] + (veg['psn_t_opt'] - veg['psn_t_min'])
    d_temp = ((psn_t_max - share['t_day']) * (share['t_day'] -
                                              veg['psn_t_min'])) / (pow(((psn_t_max - veg['psn_t_min'])/2), 2))

    if clim.loc[rstep, 'min_t'] < 6 and d_temp > 0 and share['tot_gdd'] >= gdd['gdd_fol_end']:
        '''frost effect 
        --- comment says //need to verify zzx
        '''
        d_temp = d_temp * \
            (1.0 - ((6.0 - clim.loc[rstep, 't_min'])/6.0)
             * (share['dayspan'] / 30))

    if d_temp < 0:
        d_temp = 0

    share['dvpd'] = 1.0 - veg['dvpd1'] * (pow(share['vpd'], veg['dvpd2']))
    # ten9 = 1000000000.0 # this seems silly. I'm going to use pow(10,9)

    '''In c++
    Set atmospheric co2 concentration 
    ca = clim.loc[rstep, 'co2_atm']
    I'm just applying co2 directly
    '''

    '''Co2 effect on photosynthesis'''
    '''leaf internal/external co2'''
    ci_ca_ratio = (-0.075 * veg['fol_n_con']) + 0.875

    '''ci at (present) 350ppm co2'''
    ci_350 = 350 * ci_ca_ratio

    '''ci at real year co2 level'''
    ci_elev = clim.loc[rstep, 'co2_atm'] * ci_ca_ratio

    '''Areal - rate of photosynthesis at a given atmospheric co2
    ---was there an equation for Areal at one point?'''

    '''Co2_atm conc. relative to that which occurs at co2 saturation'''
    a_rel_350 = 1.22 * ((ci_350 - 68) / (ci_350 + 136))
    a_rel_elev = 1.22 * ((ci_elev - 68) / (ci_elev + 136))
    share['d_amax'] = 1 + ((a_rel_elev - a_rel_350) / a_rel_350)

    '''Looks like gamma, ca0 are only in here for commented out equations'''
    gamma = 40  # assume a mean leaf temp. during psn of 25 oC
    ca_0 = 350
    # share['d_amax'] = (clim.loc[rstep, 'co2_atm'] - gamma) / \
    #    (clim.loc[rstep, 'co2_atm'] + 2 * gamma) * (ca_0 + 2 * gamma) / \
    #        (ca_0 - gamma)
    # (Franks,2013, New Phytologist, 197:1077-1094)

    '''Calculate co2 effect on conductance 
    and set slope, intercept for A-gs relationship '''
    if site['co2_gs_eff'] == 1:
        d_gs = share['d_amax'] / \
            ((clim.loc[rstep, 'co2_atm'] - ci_elev) / (350 - ci_350))

        # used for effect on water use efficiency
        share['d_wue'] = 1 + (1 - d_gs)
        # used to determine conductance and then ozone uptake
        gs_slope = (-1.1309 * share['d_amax']) + 1.9762
        gs_int = (0.4656 * share['d_amax']) - 0.9701

        # d_gs = share['d_amax'] / (clim.loc[rstep, 'co2_atm'] / ca_0)
        # share['d_wue'] = 1 / d_gs
        # (Franks,2013, New Phytologist, 197:1077-1094) need to refine with the downregulation
    else:
        share['d_wue'] = 1
        gs_slope = (-0.6157 * share['d_amax']) + 1.4582
        gs_int = (0.4974 * share['d_amax']) - 0.9893

    f_amax = 1
    #f_amax = 1.46 //hw

    amax = (veg['amax_a'] + veg['amax_b'] * veg['fol_n_con']) * \
        share['d_amax'] * f_amax  # nmole CO2/g Fol.sec
    # amax = (veg['amax_a'] + veg['amax_b'] * 1.8) * share['d_amax'] * f_amax # nmole CO2/g Fol.sec
    # amax = pow(10.0, (0.74 * log10(veg['fol_n_con']) - 0.57 * log10(slw_layer) + 2.96)) * share['d_amax'] # nmole CO2/g Fol.sec
    # veg['base_fol_rsp_frac'] = 0.14 - 0.002 * share['t_ave'] # longterm leaf respiration acclimation (wythers, 2013, JGR, V118, 1?4)
    # veg['rsp_q10] = 3.22 - 0.046 * (share['t_ave'] + veg['psn_t_opt'])/2 # longterm leaf respiration acclimation (wythers, 2013, JGR, V118, 1?4)
    # veg['base_fol_rsp_frac'] = 0.09
    base_fol_rsp = veg['base_fol_rsp_frac'] * amax * veg['fol_rsp_frac']
    amax = amax * veg['amax_frac']
    grs_amax = amax + base_fol_rsp
    # grs_amax: g C/g Fol/day, 12 for C atom
    grs_amax = (grs_amax * share['dvpd'] * d_temp *
                share['day_length'] * 12) / pow(10, 9)

    if grs_amax < 0:
        grs_amax = 0

    # g C/g Fol/day
    share['day_rsp'] = (base_fol_rsp * (pow(veg['rsp_q10'], ((share['t_day'] -
                                                              veg['psn_t_opt']) / 10))) * share['day_length'] * 12.0) / pow(10, 9)
    share['day_rsp'] = (base_fol_rsp * (pow(veg['rsp_q10'], ((share['t_night'] -
                                                              veg['psn_t_opt']) / 10))) * share['day_length'] * 12.0) / pow(10, 9)

    '''Initialize ozone effect'''
    can_net_psn_o3 = 0
    can_net_psn_pot = 0
    