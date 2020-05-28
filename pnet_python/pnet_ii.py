#Climate clim file
import input
import AtmEnviron

for rstep in range(input.clim_length): # steps through each climate.clim input line
    AtmEnviron.atm_environ(rstep)
    #Photo