"""
@author: Jack
Input data
"""

import pathlib
import numpy as np
import pandas as pd

## read in climate file 
path = pathlib.Path.cwd() 
path_input = path.parent / 'Input' 

#Input text file
if pathlib.Path.exists(path_input / 'pynet_input.csv'):
    input_df = pd.read_csv(path_input / 'pynet_input.csv')
else:
    print('input file does not exist')
#Climate clim file
if pathlib.Path.exists(path_input / 'climate.clim'):
    climate_df = pd.read_table(path_input / 'climate.clim')
else:
    print('climate file does not exist')

#assign input variables into structure dictionaries
#model options
modeloptions = input_df.iloc[0:2].set_index('variable')['value'].to_dict()
#site settings
site_settings = input_df.iloc[2:23].set_index('variable')['value'].to_dict()
#tree settings
tree_settings = input_df.iloc[23:78].set_index('variable')['value'].to_dict()
#management settings
management_settings = input_df.iloc[79:].set_index('variable')['value'].to_dict()
#Notice the index pattern here -- seems like [79:] is wrong -- but it works. 
 '''
 Having the data in this structure would allow us to write transparent stuff, like:
 '''
 example = tree_settings['RootTurnoverA'] * tree_settings['WoodTurnover']