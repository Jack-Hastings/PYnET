from AtmEnviron import getdays
from pnet_input import veg, clim, share

def phenology(rstep, veg, clim, share, growthphase, timestep):
    '''Phenology calculations for the PnET ecosystem model '''

    if growthphase == 1:
        '''elif instead of c++ switch case
        
        what about timestep == 2; hourly 
        '''
        if timestep == 0: #monthly timestep
            share['dayspan'] = getdays(clim.loc[rstep,'doy'], clim.loc[rstep,'year'])
        elif timestep == 1: # daily
            share['dayspan'] = 1
        else: 
            share['dayspan'] = getdays(clim.loc[rstep,'doy'], clim.loc[rstep,'year'])

        gdd = share['t_ave'] * share['dayspan']

        share['t_ave_yr'] += gdd / 365
        share['par_yr'] += clim.loc[rstep, 'par'] * share['dayspan'] / 365

        
        if gdd < 0 or clim.loc[rstep, 'doy'] < 60:
            gdd = 0 '''need modification for tropical regions'''
        
        share['tot_gdd'] += gdd

        if share['tot_gdd'] >= veg['gdd_fol_start'] and clim.loc[rstep,'doy'] < veg['senesce_start']:
            old_fol_ms = veg['fol_ms']






