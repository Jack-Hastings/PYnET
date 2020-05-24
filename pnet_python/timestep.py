#Climate clim file
import pandas
from input import climate_df

climlength = len(climate_df) #length of climate record 309 years * 12 months

climate_df[1][1]


for rstep in range(climlength):
    print(rstep)
