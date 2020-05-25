#Climate clim file
import pandas
from input import climate_df

climlength = len(climate_df) #length of climate record 309 years * 12 months
clim_ln = int(len(climate_df)/12)

rstep = 2

print (climate_df.iloc[1,rstep])

'''
A note to self: as an iterator for a dataframe, using range works well 
because it goes from 0. But, keep this in mind if using for other stuff. 
This is likely, why we see rstep + 1 in Zaixing's code. 
'''
#for rstep in range(clim_ln):
#    print(rstep)
tmin = climate_df[rstep, 3]
#tave = (tmin + tmax)/2
#tday = (tmax + tday)/2
#tnight = (tave + tmin)/2