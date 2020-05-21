import pathlib
import numpy as np
import pandas as pd




'''
Pay attention to this, 
For now, pathways are relative to the Pynet parent directory. 
If, it should be defined from the pnet child directory, the below code (path_input, etc) 
can be modified to be something like, path_input = path.parent / 'Input'
adding parent will bring it up a level to the parent directory
'''
path = pathlib.Path.cwd(); print(path)

path_input = path / 'Input' 
#path_lib = path / 'Library' # I believe this is a relict
#path_inter = path /'Inter' # this is for an intermediate directory -- ??
path_region = path /'Region'
path_out_site = path /'Result' / 'Site'
path_out_region = path /'Result' / 'Region' ; print(path_out_region)
