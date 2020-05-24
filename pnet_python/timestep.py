#Climate clim file
if pathlib.Path.exists(path_input / 'climate.clim'):
    climate_df = pd.read_table(path_input / 'climate.clim')
else:
    print('climate file does not exist')



