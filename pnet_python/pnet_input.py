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


def yearinit(share):
    '''reset certain values at the end of years year'''
	share['GDDTot'] = 0
	share['WoodMRespYr'] = 0
	share['SoilRespYr'] = 0
	share['TotTrans'] = 0
	share['TotPsn'] = 0
	share['TotGrossPsn'] = 0
	share['TotDrain'] = 0
	share['TotPrec'] = 0
	share['TotEvap'] = 0
	share['TotWater'] =0
	share['FolProdCYr'] = 0
	share['WoodProdCYr'] = 0
	share['RootProdCYr'] = 0
	share['RootMRespYr'] = 0
	share['FolGRespYr'] = 0
	share['WoodGRespYr'] = 0
	share['RootGRespYr'] = 0
	share['OldGDDFolEff'] = 0
	share['OldGDDWoodEff'] = 0
	share['PosCBalMassTot'] = 0
	share['PosCBalMassIx'] = 0
	share['Dwatertot'] = 0
	share['DwaterIx'] = 0
	share['NDrainYr']=0
	share['NetNMinYr']=0
	share['GrossNMinYr']=0
	share['PlantNUptakeYr']=0
	share['GrossNImmobYr']=0
	share['TotalLitterMYr']=0
	share['TotalLitterNYr']=0
	share['NetNitrYr']=0
	share['LightEffMin']=1
	share['SoilDecRespYr']=0
	share['WoodDecRespYr']=0
	share['NetNMinLastYr'] = share['NetNMinYr']

	share['NdepTot']=0.0 #//ZZX

	share['LightEffCBalTot']=0
	share['LightEffCBalIx']=0

	share['TaveYr']=0
	share->'PARYr'=0

	#for (int i = 0; i<51; i++)share->O3Effect[i]=0.0; 
    '''C++ above. I don't understand '''
    for i in range(51): 
        share['O3Effect'] = 1


