# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:49:32 2020

@author: Jack
"""

import pathlib
import numpy as np
import pandas as pd

## read in climate file 
path = pathlib.Path.cwd() 
path_input = path.parent / 'Input' 

#Input text file
if pathlib.Path.exists(path_input / 'input.txt'):
    input_df = pd.read_table(path_input / 'input.txt')
    print(input_df.head())
else:
    print('input file does not exist')
    
#Climate clim file
if pathlib.Path.exists(path_input / 'climate.clim'):
    climate_df = pd.read_table(path_input / 'climate.clim')
    print(climate_df.head())
else:
    print('climate file does not exist')
    

clim_vars = {
    'C02': 300,
    'NOx': 250
    }

3