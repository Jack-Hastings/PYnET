from AtmEnviron import getdays
from pnet_input import *

def phenology(rstep, share, growthphase):
    '''Phenology calculations for the PnET ecosystem model '''

    #still not sure best way to transfer over climate rstep variables
    doy = climate.loc[rstep,'DOY']
    year = climate.loc[rste, 'Year']

    if growthphase == 1:
        dayspan = getdays(doy, year)

        gdd = share['tave'] * dayspan
        tave_yr = 

    '''Assign newly created variables to share dictionary'''
        share['dayspan'] = dayspan



