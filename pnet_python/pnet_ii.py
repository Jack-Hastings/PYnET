#Climate clim file
from pnet_input import share
from AtmEnviron import atm_environ

#for rstep in range(input.clim_length): # steps through each climate.clim input line
#   AtmEnviron.atm_environ(rstep)
    #Photo


'''
for testing purposes
'''
clim_length = 5

for rstep in range(clim_length):
    atm_environ(rstep, share)

print(share)