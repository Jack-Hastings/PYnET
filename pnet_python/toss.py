share = {
    'Tave': 0,					# oC
    'Tday': 0,					# oC
    'Tnight': 0,				# oC
    'DayLength': 0,				# second
    'NightLength': 0,			# second
    'VPD': 0,					# kpa
    'dayspan': 0, 				# numbers of days of each timestep
    'GDDTot': 0,				# total growth degree days
    'OldGDDFolEff': 0,			# to calculate foliar growth
    'FolLitM': 0,				# foliar litter mass, g/m2
    'PosCBalMass': 0,			# possible C mass at balance point
    'PosCBalMassTot': 0,		# total potential mass
    'PosCBalMassIx': 0,			# total potential mass days
    'LAI': 0,					# leaf area index
    'DVPD': 0,					# vpd effect on photosynthesis
    'DayResp': 0,				# foliar respiration at daytime
    'NightResp': 0,				# foliar respiration at nighttime
    'CanopyNetPsn': 0,			# canopy net photosynthesis, gpp-foliar respiration
    'CanopyGrossPsn': 0,		# gpp
    'Dwatertot': 0,				# total water stress at growing season
    'DwaterIx': 0,				# total water stressed days
    'GrsPsnMo': 0,				# monthly gpp
    'NetPsnMo': 0,				# monthly net psn
    'FolGRespMo': 0,			# foliar growth respiration
    'WoodMRespYr': 0,			# yearly wood maintenance respiration
    'CanopyGrossPsnActMo': 0,	#monthly gpp modified by water stress and other stress
    'FolProdCYr': 0,			# foliar npp, g C m-2
    'FolProdCMo': 0,			# foliar npp each time step, g C m-2
    'FolGRespYr': 0,			# foliar yearly growth respiration, g C m-2
    'RootProdCYr': 0,			# root npp, g C m-2
    'RootMRespYr': 0,			# root yearly maintenance respiration, g C m-2
    'RootGRespYr': 0,			# root yearly growth respiration, g C m-2
    'SoilRespMo': 0,			# soil respiration, g C m-2
    'SoilRespYr': 0,			# soil yearly respiration, g C m-2
    'OldGDDWoodEff': 0,			# to calculate wood growth
    'WoodProdCYr': 0,			# wood npp, g C m-2
    'WoodGRespYr': 0,			# wood yearly growth respiration, g C m-2
    'TotPsn': 0,				# total net psn
    'MeanSoilMoistEff': 0,		# soil moisture effect on som decay
    'Drainage': 0,				# water drainage, as runoff + leaching
    'TotDrain': 0,				# total drainage
    'TotEvap': 0,				# total evaporation
    'TotTrans': 0,				# total transpiration
    'TotPrec': 0,				# total precipitation
    'TotWater': 0,				# total soil water
    'TotGrossPsn': 0,			# total gpp
    'NPPFolYr': 0,				# foliar npp, g dry matter m-2
    'NPPWoodYr': 0,				# wood npp, g dry matter m-2
    'NPPRootYr': 0,				# root npp, g dry matter m-2
    'ET': 0,					# ET
    'NEP': 0,					# net ecosystem production, -NEE
    'NetCBal': 0,				# net C balance, NEE
    'SoilDecResp': 0,			# soil decomposition
    'BudN': 0,					# bud N or foliar total N
    'SoilDecRespYr': 0,			# yearly soil decomposition
    'WoodDecRespYr': 0,			# yearly deadwood decay loss as CO2
    'DelAmax': 0,				# Amax adjustor for CO2 effect
    'DWUE': 0,					# WUE adjustor for CO2 effect
    'CanopyDO3Pot': 0,			# O3 effect on photosynthesis for the whole canopy
    'DroughtO3Frac': 0,			# drought effect on O3 effect
    'TotO3Dose': 0,				# total O3 dose
    'RootMassN': 0,				#root N
    'TotalLitterMYr': 0,		# total yearly litter mass
    'TotalLitterNYr': 0,		# total yearly litter N
    'GrossNImmobYr': 0,			# total yearly gross N immoblized
    'GrossNMinYr': 0,			# total yearly gross N mineralization
    'PlantNUptakeYr': 0,		# yearly plant uptake N
    'NetNitrYr': 0,				# yearly net Nitrification rate
    'NetNMinYr': 0,				# yearly net mineralization rate
    'FracDrain': 0,				# proportion of drainage to total water
    'NDrainYr': 0,				# yearly N drained out
    'NDrain': 0,				# drained N, gN m-2
    'NDrainMgL': 0,				# drained N concentration in water, mgN l-1
    'WoodDecResp': 0,			# wood decay
    'TotalLitterM': 0,			# total litter mass
    'TotalLitterN': 0,			# total litter N
    'FolN': 0,					# total foliar N
    'FolC': 0,					# total foliar C
    'TotalN': 0,				# total N
    'TotalM': 0,				# total mass
    'NO3': 0,					# NO3 content
    'NH4': 0,					# NH4 content
    'FolNConOld': 0, 			# to store FolN for output.
    'NdepTot': 0,				# total N deposition
    #Shared variables with initial conditions
    'FolMass': 0,   # FolMass=veg.FolMassMin: 0,   In PnET-Day only,g/m2
    'BudC': 0,    # BudC=(veg.FolMassMax- FolMass)*veg.CFracBiomass: 0,  In PnET-Day only
    'Water': 0,		            # soil water
    'DeadWoodM': 0,	            # dead wood mass
    'WoodC': 0,		            #  wood C pool for wood growth
    'PlantC': 0,		        # plant C pool to store non structure C
    'RootC': 0,		            # Root C pool for root dynamic growth
    'LightEffMin': 0,	        # minimum light effect for next year foliar growth
    'NRatio': 0,		    	# N stress index
    'PlantN': 0,			    # plant N pool
    'WoodMass': 0,		        # wood mass
    'RootMass': 0,		        # root mass
    'HOM': 0,			    	# soil som
    'HON': 0,				    # soil son
    'RootNSinkEff': 0,	        # root N uptake capability
    'WUEO3Eff': 0,		        # O3 effect on WUE
    'WoodMassN': 0,		        # live wood total N
    'DeadWoodN': 0,		        # dead wood total N
    'NRatioNit': 0,		        # Nitrification constant determined by Nratio
    'NetNMinLastYr': 0, 	    # previous year net N mineralizatio rate
    'DWater': 0,	  		    # water stress for plant growth
    'LightEffCBal': 0,	        # light effect at foliar light compensation point.
    'LightEffCBalTot': 0,	    # total light effect at foliar light compensation point at growing season
    'LightEffCBalIx': 0,	    # number of days for LightEffCBal > 0.
    'O3Effect': [0] * 50,	    # O3 effect for each canopy layer
    'avgPCBM': 0,			    # average light effect
    'AvgDWater': 0,		        # average water stress
    'TaveYr': 0,			    # annual average air T, degree
    'PARYr': 0,			        # annual average air Par, umol m-2 s-1 at daytime
}
