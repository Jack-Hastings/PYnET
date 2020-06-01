"""
@author: Jack Hastings
Input data
"""

import pathlib
import pandas as pd

'''No hardcode paths'''
path = pathlib.Path.cwd()
path_input = path.parent / 'Input'

'''Read in input and climate file.'''
# Input text file.
input = pd.read_csv(path_input / 'pynet_input.csv')

# Climate clim file
climate = pd.read_table(path_input / 'climate.clim')


'''assign a climate length to be used in the rstep looping'''
clim_length = len(climate)


'''Assign the input data to dictionaries

I've done this to mimic the transparency of the c++ structs.
This may or may not be a good idea. Can easily rip it out.
'''
# model options
modeloptions = input.iloc[0:2].set_index('variable')['value'].to_dict()
# site settings
site_settings = input.iloc[2:23].set_index('variable')['value'].to_dict()
# tree settings
tree_settings = input.iloc[23:78].set_index('variable')['value'].to_dict()
# management settings
management_settings = input.iloc[79:].set_index('variable')['value'].to_dict()
# Notice the index pattern here -- seems like [79:] is wrong -- but it works.


'''Define share dictionary to hold the outputs of each function.

Values are initially set to zero.

Naming convention:
*Changed to comply with pep8: Switch from CamelCase to snake_case.
*Simplified where possible. e.g. gross -> grs
*Standardized where possible. e.g. Mass, m -> ms; tot to front
*There is an inconsistency with tot & yearly use. When should we use tot?
*Min reserved from mineralization. Minimum changed to minim

#comments retained from C++
//OldName

Maybe have a csv/txt where these variables are defined.
Could read it in and modify as necessary.

'''
share = {
    't_ave': 0,					# oC    //Tave
    't_day': 0,					# oC    //Tday
    't_night': 0,				# oC    //Tnight
    'day_length': 0,			# second    //DayLength
    'night_length': 0,			# second    //NightLength
    'vpd': 0,					# kpa   //VPD
    'dayspan': 0, 				# numbers of days of each timestep  //dayspan
    'tot_gdd': 0,				# total growth degree days  //GDDTot
    'old_gdd_fol_eff': 0,		# to calculate foliar growth    //OldGDDFolEff
    'fol_lit_m': 0,				# foliar litter mass, g/m2  //FolLitM
    'pos_c_bal_ms': 0,			# possible C mass at balance point  //PosCBalMass
    'tot_pos_c_bal_ms': 0,		# total potential mass  //PosCBalMassTot
    'tot_pos_c_bal_ms_ix': 0,   # total potential mass days //PosCBalMassIx
    'lai': 0,					# leaf area index   //LAI
    'd_vpd': 0,					# vpd effect on photosynthesis  //DVPD
    'day_rsp': 0,				# foliar respiration at daytime //DayResp
    'night_rsp': 0,				# foliar respiration at nighttime   //NightResp
    'can_net_psn': 0,			# can. net photosyn., gpp-foliar respiration    //CanopyNetPsn
    'can_grs_psn': 0,		   	# gpp   //CanopyGrossPsn
    'tot_d_water': 0,			# total water stress at growing season  //Dwatertot
    'tot_d_water_ix': 0,		# total water stressed days //DwaterIx
    'grs_psn_mo': 0,			# monthly gpp   //GrsPsnMo
    'net_psn_mo': 0,			# monthly net psn   //NetPsnMo
    'fol_g_rsp_mo': 0,			# foliar growth respiration //FolGRespMo
    'wood_maint_rsp_yr': 0,		# yearly wood maintenance respiration   //WoodMRespYr
    # mo. gpp mod. by water stress, other stress    
    'can_grs_psn_act_mo': 0,    # //CanopyGrossPsnActMo
    'fol_prod_c_yr': 0,			# foliar npp, g C m-2   //FolProdCYr
    'fol_prod_c_mo': 0,			# foliar npp each time step, g C m-2    //FolProdCMo
    'fol_g_rsp_yr': 0,			# foliar yearly growth respiration, g C m-2 //FolGRespYr
    'root_prod_c_yr': 0,		# root npp, g C m-2 //RootProdCYr
    'root_maint_rsp_yr': 0,		# root yearly maintenance respiration, g C m-2  //RootMRespYr
    'root_g_rsp_yr': 0,			# root yearly growth respiration, g C m-2   //RootGRespYr
    'soil_rsp_mo': 0,			# soil respiration, g C m-2 //SoilRespMo
    'soil_rsp_yr': 0,			# soil yearly respiration, g C m-2  //SoilRespYr
    'old_gdd_wood_eff': 0,		# to calculate wood growth  //OldGDDWoodEff
    'wood_prod_c_yr': 0,		# wood npp, g C m-2 //WoodProdCYr
    'wood_g_rsp_yr': 0,			# wood yearly growth respiration, g C m-2   //WoodGRespYr
    'tot_psn': 0,				# total net psn //TotPsn
    'mean_soil_moist_eff': 0,   # soil moisture effect on som decay //MeanSoilMoistEff
    'drainage': 0,				# water drainage, as runoff + leaching  //Drainage
    'tot_drain': 0,				# total drainage    //TotDrain
    'tot_evap': 0,				# total evaporation //TotEvap
    'tot_trans': 0,				# total transpiration   //TotTrans
    'tot_prec': 0,				# total precipitation   //TotPrec
    'tot_water': 0,				# total soil water  //TotWater
    'tot_grs_psn': 0,			# total gpp //TotGrossPsn
    'npp_fol_yr': 0,			# foliar npp, g dry matter m-2  //NPPFolYr
    'npp_wood_yr': 0,			# wood npp, g dry matter m-2    //NPPWoodYr
    'npp_root_yr': 0,			# root npp, g dry matter m-2    //NPPRootYr
    'et': 0,					# ET    //ET
    'nep': 0,					# net ecosystem production, -NEE    //NEP
    'net_c_bal': 0,				# net C balance, NEE    //NetCBal
    'soil_dec_rsp': 0,			# soil decomposition    //SoilDecResp
    'bud_n': 0,				    # bud N or foliar total N   //BudN
    'soil_dec_rsp_yr': 0,		# yearly soil decomposition //SoilDecRespYr
    'wood_dec_rsp_yr': 0,		# yearly deadwood decay loss as CO2 //WoodDecRespYr
    'd_amax': 0,				# Amax adjustor for CO2 effect  //DelAmax
    'd_wue': 0,					# WUE adjustor for CO2 effect   //DWUE
    'can_d_o3_pot': 0,			# O3 effect on photosynthesis for the whole canopy  //CanopyDO3Pot
    'drought_o3_frac': 0,		# drought effect on O3 effect   //DroughtO3Frac
    'tot_o3_dose': 0,			# total O3 dose //TotO3Dose
    'root_ms_n': 0,             # root N    //RootMassN
    'tot_lit_ms_yr': 0,		 	# total yearly litter mass  //TotalLitterMYr
    'tot_lit_n_yr': 0,		 	# total yearly litter N //TotalLitterNYr
    'tot_grs_n_immob_yr': 0,    # total yearly gross N immoblized   //GrossNImmobYr
    'tot_grs_n_min_yr': 0,		# total yearly gross N mineralization   //GrossNMinYr
    'plant_n_uptake_yr': 0,		# yearly plant uptake N //PlantNUptakeYr
    'net_nitr_yr': 0,			# yearly net Nitrification rate //NetNitrYr
    'net_n_min_yr': 0,			# yearly net mineralization rate    //NetNMinYr
    'frac_drain': 0,			# proportion of drainage to total water //FracDrain
    'n_drain_yr': 0,			# yearly N drained out  //NDrainYr
    'n_drain': 0,				# drained N, gN m-2 //NDrain
    'n_drain_mgl': 0,			# drained N concentration in water, mgN l-1 //NDrainMgL
    'wood_dec_rsp': 0,			# wood decay    //WoodDecResp
    'tot_lit_ms': 0,			# total litter mass //TotalLitterM
    'tot_lit_n': 0,			   	# total litter N    //TotalLitterN
    'tot_fol_n': 0,				# total foliar N    //FolN
    'tot_fol_c': 0,				# total foliar C    //FolC
    'tot_n': 0,				    # total N   //TotalN
    'tot_ms': 0,				# total mass    //TotalM
    'no3': 0,					# NO3 content   //NO3
    'nh4': 0,					# NH4 content   //NH4
    'fol_n_con_old': 0, 		# to store FolN for output. //FolNConOld
    'tot_n_dep': 0,				# total N deposition    //NdepTot
    'soil_water': 0,		    # soil water    //Water  '''from input'''
    'dead_wood_ms': 0,	        # dead wood mass    //DeadWoodM '''from input'''
    'wood_c': 0,                # wood C pool for wood growth   //WoodC '''from input'''
    'plant_c': 0,		        # plant C pool to store non structure C //PlantC    '''from input'''
    'root_c': 0,		        # Root C pool for root dynamic growth   //RootC '''wood_c/3'''
    'light_eff_minim': 0,	    # minimum light effect for next year foliar growth  //LightEffMin '''hardwired as 1?'''
    'n_ratio': 0,		    	# N stress index    //NRatio    '''from input''
    'plant_n': 0,			    # plant N pool  //PlantN    '''from input'''
    'wood_ms': 0,		        # wood mass //WoodMass  '''from input'''
    'root_ms': 0,		        # root mass //RootMass  '''from input'''
    'hom': 0,			    	# soil som  //HOM   '''from input'''
    'hon': 0,				    # soil son  //HON   '''from input''
    'root_n_sink_eff': 0,	    # root N uptake capability  //RootNSinkEff  '''hardwired as 0.5'''
    'wue_o3_eff': 0,		    # O3 effect on WUE  //WUEO3EFF  '''from input --dif name?'''
    'tot_wood_ms_n': 0,		    # live wood total N //WoodMassN     '''modified'''
    'tot_dead_wood_n': 0,		# dead wood total N //DeadWoodN '''modified'''
    'n_ratio_nit': 0,		    # Nitrification constant determined by Nratio   //NRatioNit
    'net_n_min_last_yr': 0, 	# previous year net N mineralizatio rate    //NetNMinLastYr
    'd_water': 0,	  		    # water stress for plant growth //dwater '''hardwired'''
    'light_eff_c_bal': 0,       # light effect at fol. light comp. point.   //LightEffCBal  '''where are these used?'''
    'tot_light_eff_c_bal': 0,   # tot. light eff. at fol. light comp. in GS //LightEffCBalTot
    'light_eff_c_bal_ix': 0,    # number of days for LightEffCBal > 0.  //LightEffCBalIx
    'o3_effect': [0] * 50,	    # O3 effect for each canopy layer   //O3Effect
    'avg_pcbm': 0,			    # average light effect  //avgPCBM
    'avg_d_water': 0,		    # average water stress  //AvgDWater
    't_ave_yr': 0,			    # annual average air T, degree  //TaveYr
    'par_yr': 0,			    # annual average air Par, umol m-2 s-1 at daytime   //PARYr
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
    share['net_n_min_last_yr'] = share['net_n_min_yr']  # Won't this be zero?
    share['tot_n_dep'] = 0.0  # //ZZX
    share['tot_light_eff_c_bal'] = 0
    share['light_eff_c_bal_ix'] = 0
    share['t_ave_yr'] = 0
    share['par_yr'] = 0
    ''' reset all 50 layers '''
    for i in range(0, 10):
        share['o3_effect'][i] = 0
