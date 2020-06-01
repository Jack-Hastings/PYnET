from math import * #this is the same C/C++ Math Library
from pnet_input import *

def atm_environ(rstep, share): # should I have the other dicts as input?
    '''
    What if for readability we have the the called input variables pulled in 
    first from input, and at the end have another chunk of code 
    that sends everything to the shared dictionary? 
    Functionally, this would be the same, but it'd increase readabilty...
    I could also do the same with stuff like site_settings['Latitude'].
    '''
    #r
    tmin = climate.loc[rstep,'MinT(oc)'] 
    tmax = climate.loc[rstep,'MaxT(oc)']
    doy = climate.loc[rstep,'DOY']

    tave = (tmin+ tmax)/2.0
    tday = (tmax + tave)/2.0
    tnight =(tave + tmin)/2.0

    latrad = site_settings['Latitude'] * (2.0 * pi)/ 360
    ''' r is a hold over from matlab. Never used. delete? '''
    r = 1 - (0.0167 * cos(0.0172 * (doy - 3))) 
    z = (0.39785 * sin(4.868961 + 0.017203 * doy + 0.033446 *
     sin(6.224111 + 0.017202 * doy)))
    # I want to put in comments to reference each equation
    if fabs(z) < 0.7:
        decl = atan(z / (sqrt(1.0 - pow(z, 2))))
    else:
        decl = pi / 2.0 - atan(sqrt(1 - pow(z,2)) / z)

    if fabs(latrad) >= (pi / 2):
        if (site_settings['Latitude'] < 0):
            latrad = (-1.0) * (pi / 2.0 - 0.01)
        else: 
            latrad = (1.0) * (pi / 2.0 - 0.01)
    
    z2 = -tan(decl) * tan(latrad)

    if z2 >= 1.0:
        h = 0
    elif z2 <= -1.0: 
        h = pi
    else: 
        TA = fabs(z2)
        if TA < 0.7:
            AC = 1.570796 - atan(TA / sqrt(1.0 - pow(TA,2)))
        else:
            AC = atan(sqrt(1 - pow(TA, 2)) / TA)
        if z2 < 0:
            h = pi - AC
        else:
            h = AC 
    
    hr = 2.0 * (h * 24.0) / (2.0 * pi) # hours
    daylength = 3600 * hr # seconds
    nightlength = 3600 * (24.0 - hr) #seconds

    '''
    Assign shared variables to the share dictionary
    '''
    share['tave'] = tave
    share['tday'] = tday
    share['tnight'] = tnight
    share['daylength'] = daylength
    share['nightlength'] = nightlength
    
    return(share)


def getdays(doy, year):
    if doy > 367 or doy < 1:
        print("Cannot convert the number to date")
        return 0

    '''
    Note that indexing starts at zero. Jan = 0, Feb = 1, etc.
    This differs from c++ just barely because of that
    '''
    days = [31] * 12 #start with 31 days, specify from here
    days[1] = 28 # feb
    '''didn't know this about leap years...'''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days[1] = 29
    days[3] = days[5] = days[8] = days[10] = 30 #april, june, sept., Nov.

    i = 0
    while doy > days[i]:
        doy -=days[i]
        i +=1

    return days[i]

def getmonth(doy, year):
    if doy > 367 or doy < 1:
        print("Cannot convert the number to date")
        return 0

    '''
    Note that indexing starts at zero. Jan = 0, Feb = 1, etc.
    This differs from c++ just barely because of that
    '''
    days = [31] * 12 #start with 31 days, specify from here
    days[1] = 28 # feb
    '''didn't know this about leap years...'''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days[1] = 29
    days[3] = days[5] = days[8] = days[10] = 30 #april, june, sept., Nov.

    i = 0
    while doy > days[i]:
        doy -=days[i]
        i +=1

    return i #note subtle difference between getday and getmonth

def is_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0