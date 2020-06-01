"""
@author: Jack
Input data
"""

import pathlib
import pandas as pd

'''No hardcode paths'''
path = pathlib.Path.cwd() 
path_input = path.parent / 'Input' 

'''Read in input and climate file.'''
#Input text file. 
input = pd.read_csv(path_input / 'pynet_input.csv')

#Climate clim file
climate = pd.read_table(path_input / 'climate.clim')


'''assign a climate length to be used in the rstep looping'''
clim_length = len(climate) 


'''Assign the input data to dictionaries

I've done this to mimic the transparency of the c++ structs. 
This may or may not be a good idea. Can easily rip it out.
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


'''Define share dictionary to hold the outputs of each function.

Values are initially set to zero.

Naming convention:
*Changed to comply with pep8: Switch from CamelCase to snake_case. 
*Simplified where possible. e.g. gross -> grs
*Standardized where possible. e.g. Mass, m -> ms; tot to front
*There is an inconsistency with tot & yearly use. When should we use tot?
*Min reserved from mineralization. Minimum changed to minim

'''
share = {
    't_ave': 0,					# oC
    't_day': 0,					# oC
    't_night': 0,				# oC
    'day_length': 0,			# second
    'night_length': 0,			# second
    'vpd': 0,					# kpa
    'dayspan': 0, 				# numbers of days of each timestep
    'tot_gdd': 0,				# total growth degree days
    'old_gdd_fol_eff': 0,		# to calculate foliar growth
    'fol_lit_m': 0,				# foliar litter mass, g/m2
    'pos_c_bal_ms': 0,		    # possible C mass at balance point
    'tot_pos_c_bal_ms': 0,		# total potential mass
    'tot_pos_c_bal_ms_ix': 0,	# total potential mass days
    'lai': 0,					# leaf area index
    'd_vpd': 0,					# vpd effect on photosynthesis
    'day_rsp': 0,				# foliar respiration at daytime
    'night_rsp': 0,				# foliar respiration at nighttime
    'can_net_psn': 0,			# canopy net photosynthesis, gpp-foliar respiration
    'can_grs_psn': 0,		    # gpp
    'tot_d_water': 0,			# total water stress at growing season
    'tot_d_water_ix': 0,		# total water stressed days
    'grs_psn_mo': 0,			# monthly gpp
    'net_psn_mo': 0,			# monthly net psn
    'fol_g_rsp_mo': 0,			# foliar growth respiration
    'wood_maint_rsp_yr': 0,		# yearly wood maintenance respiration
    'can_grs_psn_act_mo': 0,	#monthly gpp modified by water stress and other stress
    'fol_prod_c_yr': 0,			# foliar npp, g C m-2
    'fol_prod_c_mo': 0,			# foliar npp each time step, g C m-2
    'fol_g_rsp_yr': 0,			# foliar yearly growth respiration, g C m-2
    'root_prod_c_yr': 0,		# root npp, g C m-2
    'root_maint_rsp_yr': 0,		# root yearly maintenance respiration, g C m-2
    'root_g_rsp_yr': 0,			# root yearly growth respiration, g C m-2
    'soil_rsp_mo': 0,			# soil respiration, g C m-2
    'soil_rsp_yr': 0,			# soil yearly respiration, g C m-2
    'old_gdd_wood_eff': 0,		# to calculate wood growth
    'wood_prod_c_yr': 0,		# wood npp, g C m-2
    'wood_g_rsp_yr': 0,			# wood yearly growth respiration, g C m-2
    'tot_psn': 0,				# total net psn
    'mean_soil_moist_eff': 0,	# soil moisture effect on som decay
    'drainage': 0,				# water drainage, as runoff + leaching
    'tot_drain': 0,				# total drainage
    'tot_evap': 0,				# total evaporation
    'tot_trans': 0,				# total transpiration
    'tot_prec': 0,				# total precipitation
    'tot_water': 0,				# total soil water
    'tot_grs_psn': 0,			# total gpp
    'npp_fol_yr': 0,			# foliar npp, g dry matter m-2
    'npp_wood_yr': 0,			# wood npp, g dry matter m-2
    'npp_root_yr': 0,			# root npp, g dry matter m-2
    'et': 0,					# ET
    'nep': 0,					# net ecosystem production, -NEE
    'net_c_bal': 0,				# net C balance, NEE
    'soil_dec_rsp': 0,			# soil decomposition
    'tot_bud_n': 0,				# bud N or foliar total N
    'soil_dec_rsp_yr': 0,		# yearly soil decomposition
    'wood_dec_rsp_yr': 0,		# yearly deadwood decay loss as CO2
    'd_amax': 0,				# Amax adjustor for CO2 effect
    'd_wue': 0,					# WUE adjustor for CO2 effect
    'can_d_o3_pot': 0,			# O3 effect on photosynthesis for the whole canopy
    'drought_o3_frac': 0,		# drought effect on O3 effect
    'tot_o3_dose': 0,			# total O3 dose
    'root_ms_n': 0,				#root N
    'tot_lit_ms_yr': 0,		    # total yearly litter mass
    'tot_lit_n_yr': 0,		    # total yearly litter N
    'tot_grs_n_immob_yr': 0,	# total yearly gross N immoblized
    'tot_grs_n_min_yr': 0,		# total yearly gross N mineralization
    'plant_n_uptake_yr': 0,		# yearly plant uptake N
    'net_nitr_yr': 0,			# yearly net Nitrification rate
    'net_n_min_yr': 0,			# yearly net mineralization rate
    'frac_drain': 0,			# proportion of drainage to total water
    'n_drain_yr': 0,			# yearly N drained out
    'n_drain': 0,				# drained N, gN m-2
    'n_drain_mgl': 0,			# drained N concentration in water, mgN l-1
    'wood_dec_rsp': 0,			# wood decay
    'tot_lit_ms': 0,			# total litter mass
    'tot_lit_n': 0,			    # total litter N
    'tot_fol_n': 0,				# total foliar N 
    'tot_fol_c': 0,				# total foliar C
    'tot_n': 0,				    # total N
    'tot_ms': 0,				# total mass
    'no3': 0,					# NO3 content
    'nh4': 0,					# NH4 content
    'fol_n_con_old': 0, 		# to store FolN for output.
    'tot_n_dep': 0,				# total N deposition
    #Shared variables with initial conditions
    'fol_ms': 0,   # FolMass=veg.FolMassMin: 0,   In PnET-Day only,g/m2
    'bud_c': 0,    # BudC=(veg.FolMassMax- FolMass)*veg.CFracBiomass: 0,  In PnET-Day only
    'water': 0,		            # soil water
    'dead_wood_ms': 0,	        # dead wood mass
    'wood_c': 0,		        #  wood C pool for wood growth
    'plant_c': 0,		        # plant C pool to store non structure C
    'root_c': 0,		        # Root C pool for root dynamic growth
    'light_eff_minim': 0,	    # minimum light effect for next year foliar growth
    'n_ratio': 0,		    	# N stress index
    'plant_n': 0,			    # plant N pool
    'wood_ms': 0,		        # wood mass
    'root_ms': 0,		        # root mass
    'hom': 0,			    	# soil som
    'hon': 0,				    # soil son
    'root_n_sink_eff': 0,	    # root N uptake capability
    'wue_o3_eff': 0,		    # O3 effect on WUE
    'tot_wood_ms_n': 0,		    # live wood total N
    'tot_dead_wood_n': 0,		# dead wood total N
    'n_ratio_nit': 0,		    # Nitrification constant determined by Nratio
    'net_n_min_last_yr': 0, 	# previous year net N mineralizatio rate
    'd_water': 0,	  		    # water stress for plant growth
    'light_eff_c_bal': 0,	    # light effect at foliar light compensation point.
    'tot_light_eff_c_bal': 0,	# total light effect at foliar light compensation point at growing season
    'light_eff_c_bal_ix': 0,	# number of days for LightEffCBal > 0.
    'o3_effect': [0] * 50,	    # O3 effect for each canopy layer
    'avg_pcbm': 0,			    # average light effect
    'avg_d_water': 0,		    # average water stress
    't_ave_yr': 0,			    # annual average air T, degree
    'par_yr': 0,			    # annual average air Par, umol m-2 s-1 at daytime
}

def yearinit(share):
	'''reset certain values at the end of years year'''
	share['tot_gdd'] = 0
	share['wood_maint_rsp_yr'] = 0 
	share['soil_rsp_yr'] = 0
	share['tot_trans'] = 0
	share['tot_psn'] = 0
	share['tot_grs_psn'] = 0 
	share['tot_drain'] = 0 
	share['tot_prec'] = 0
	share['tot_evap'] = 0
	share['tot_water'] = 0
	share['fol_prod_c_yr'] = 0
	share['wood_prod_c_yr'] = 0
	share['root_prod_c_yr'] = 0
	share['root_maint_rsp_yr'] = 0
	share['fol_g_rsp_yr'] = 0
	share['wood_g_rsp_yr'] = 0
	share['root_g_rsp_yr'] = 0
	share['old_gdd_fol_eff'] = 0
	share['old_gdd_wood_eff'] = 0
	share['tot_pos_c_bal_ms'] = 0
	share['tot_pos_c_bal_ms_ix'] = 0
	share['tot_d_water'] = 0
	share['tot_d_water_ix'] = 0
	share['n_drain_yr'] = 0
	share['net_n_min_yr'] = 0
	share['tot_grs_n_min_yr'] = 0
	share['plant_n_uptake_yr'] = 0 
	share['tot_grs_n_immob_yr'] = 0
	share['tot_lit_ms_yr'] = 0
	share['tot_lit_n_yr'] = 0
	share['net_nitr_yr'] = 0
	share['light_eff_minim'] = 1
	share['soil_dec_rsp_yr'] = 0
	share['wood_dec_rsp_yr'] = 0
    share['net_n_min_last_yr'] = share['net_n_min_yr'] ''' wont this line  just set it to zero? '''
	share['tot_n_dep'] = 0.0 #//ZZX

	share['tot_light_eff_c_bal'] = 0
	share['light_eff_c_bal_ix'] = 0

	share['t_ave_yr'] = 0
	share['par_yr'] = 0

	#for (int i = 0; i<51; i++)share->O3Effect[i]=0.0; 
