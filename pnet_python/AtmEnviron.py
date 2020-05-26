import math
import input

rstep = 10

toss1 = input.climate
toss2 = input.input
def atm_environ(rstep):
    #pull tmin, tmax from the climate input file by rstep
    #rstep is a holdover from C++ it's the iterator 
    tmin = input.climate.loc[rstep,'MinT(oc)'] 
    tmax = input.climate.loc[rstep,'MaxT(oc)']

    tave = (tmin+ tmax)/2
    tday = (tmax + tave)/2
    tnight =(tave + tmin)/2

    print(tave,tday,tnight)

