from math import atan, pi, cos, 
#this is the same C library used in PnET C++ check this.
import input

rstep = 10

toss1 = input.climate
toss2 = input.input
toss3 = input.site_settings
def atm_environ(rstep):
    '''
    Initially define all variables iteratively pulled from cliamte?
    I think this helps clean up the code below. 
    rstep is an iterator, which steps through each line of the climate file 
    rstep is monthly here? the climate file has one doy per month.
    what about stuff called from the input dictionaries? e.g. latrad
    we can remove input. if initially we call 'from input import *' 
    
    '''
    tmin = input.climate.loc[rstep,'MinT(oc)'] 
    tmax = input.climate.loc[rstep,'MaxT(oc)']
    doy = input.climate.loc[rstep,'DOY']

    tave = (tmin+ tmax)/2.0
    tday = (tmax + tave)/2.0
    tnight =(tave + tmin)/2.0

    latrad = input.site_settings['Latitude'] * (2.0 * math.pi)/ 360
    r = 1 - (0.0167 * math.cos(0.0172 * (doy - 3)))
    z = (0.39785 * math.sin(4.868961 + 0.017203 * doy + 0.033446 *
     math.sin(6.224111 + 0.017202 * doy)))
    # I want to put in comments to reference each equation
    if math.fabs(z) < 0.7:
        decl = math.atan(z / (math.sqrt(1.0 - math.pow(z, 2))))
    else:
        decl = math.pi / 2.0 - math.atan(math.sqrt(1 - math.pow(z,2)) / z)

    if math.fabs(latrad) >= (math.pi / 2):
        if (input.site_settings['Latitude'] < 0):
            latrad = (-1.0) * (math.pi / 2.0 - 0.01)
        else: 
            latrad = (1.0) * (math.pi / 2.0 - 0.01)
    
    z2 = -math.tan(decl) * math.tan(latrad)

    if z2 >= 1.0:
        h = 0
    elif z2 <= -1.0: 
        h = math.pi
    else: 
        TA = math.fabs(z2)
        if TA < 0.7:
            AC = 1.570796 - math.atan(TA / math.sqrt(1.0 - math.pow(TA,2)))
        else:
            AC = math.atan(math.sqrt(1 - math.pow(TA, 2)) / TA)
        if z2 < 0:
            h = math.pi - AC
        else:
            h = AC 
    
    hr = 2.0 * (h * 24.0) / (2.0 * math.pi) # hours
    daylength = 3600 * hr # seconds
    nightlength = 3600 * (24.0 - hr) #seconds

    #what do I have to return?


#! come back to these functions
def getdays(year, doy):
    for month in range(1,13): 
        print(month)