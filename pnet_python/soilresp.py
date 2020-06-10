from math import exp


def soilresp(veg, share, rstep):
    '''soil respiration routine for pnet ii only?'''

    #end of equation ... whats the point of the plus zero?
    share['soil_rsp_mo'] = veg['soil_rsp_a'] * exp(veg['soil_rsp_b'] * (share['t_ave'] + 0)) # g C/m2.mo
    share['soil_rsp_mo'] = share['soil_rsp_mo'] * share['mean_soil_moist_eff']
    share['soil_rsp_mo'] = share['soil_rsp_mo'] * (share['dayspan'] / 30.5) #g C/m2.DaySpan
    share['soil_rsp_yr'] = share['soil_rsp_yr'] + share['soil_rsp_mo']

