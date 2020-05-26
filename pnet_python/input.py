"""
@author: Jack
Input data
"""

import pathlib
import pandas as pd

'''No hardcode paths -- this is giving me issues. 
Need to figure out where everything should be called from.
path_input is wrong if I don't call everything form pnet_python...
'''
path = pathlib.Path.cwd() 
path_input = path.parent / 'Input' 

#Input text file
if pathlib.Path.exists(path_input / 'pynet_input.csv'):
    input = pd.read_csv(path_input / 'pynet_input.csv')
else:
    print('input file does not exist')
#Climate clim file
if pathlib.Path.exists(path_input / 'climate.clim'):
    climate = pd.read_table(path_input / 'climate.clim')
else:
    print('climate file does not exist')
#assign input variables into structure dictionaries --- not sure this is a good idea, but it'd be transparent.
#model options
modeloptions = input.iloc[0:2].set_index('variable')['value'].to_dict()
#site settings
site_settings = input.iloc[2:23].set_index('variable')['value'].to_dict()
#tree settings
tree_settings = input.iloc[23:78].set_index('variable')['value'].to_dict()
#management settings
management_settings = input.iloc[79:].set_index('variable')['value'].to_dict()
#Notice the index pattern here -- seems like [79:] is wrong -- but it works. 

#Having the data in this structure would allow us to write transparent stuff, like:
example = tree_settings['RootTurnoverA'] * tree_settings['WoodTurnover']



