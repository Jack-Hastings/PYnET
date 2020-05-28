"""
@author: Jack
Input data
"""

import pathlib
import pandas as pd

'''No hardcode paths'''
path = pathlib.Path.cwd() 
path_input = path.parent / 'Input' 

'''
Read in input and climate file.
I could rip out the if/else stuff. Not necessary 
'''
#Input text file. 
if pathlib.Path.exists(path_input / 'pynet_input.csv'):
    input = pd.read_csv(path_input / 'pynet_input.csv')
else:
    print('input file does not exist')
#Climate clim file
if pathlib.Path.exists(path_input / 'climate.clim'):
    climate = pd.read_table(path_input / 'climate.clim')
else:
    print('climate file does not exist')

'''assign a climate length to be used in the rstep looping'''
clim_length = len(climate) 


'''
Below I assign the input data to dictionaries to mimic the transparency 
of the c++ structs. This may or may not be a good idea. Can easily rip it out.
'''
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

'''define empty share dictionary to hold the outputs of each function'''

share = {}



