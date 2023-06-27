import os
import sys

sys.path.append("/glade/work/mollyw/Projects/sit_variability/cmip6/cmip6_downloader")

models = ["ACCESS-CM2",
         "ACCESS-ESM1-5",
         "AWI-CM-1-1-MR",
         "AWI-ESM-1-1-LR",
         #"BCC-CSM2-MR",
         #"BCC-ESM1",
         #"CAMS-CSM1-0",
         #"CAS-ESM2-0",
         "CESM2",
         "CESM2-FV2",
         "CESM2-WACCM",
         "CESM2-WACCM-FV2",
         #"CIESM",
         #"CMCC-CM2-HR4",
         "CMCC-CM2-SR5",
         "CMCC-ESM2",
         #"CNRM-CM6-1",
         #"CNRM-CM6-1-HR",
         #"CNRM-ESM2-1",
         "E3SM-1-0",
         "EC-Earth3",
         "EC-Earth3-AerChem",
         "EC-Earth3-CC",
         "EC-Earth3-Veg",
         #"FGOALS-f3-L",
         #"FGOALS-g3",
         #"FIO-ESM-2-0",
         "GFDL-CM4",
         "GFDL-ESM4",
         "GISS-E2-2-G",
         "GISS-E2-2-H",
         #"HadGEM3-GC31-MM",
         #"HadGEM3-GC31-LL",
         "ICON-ESM-LR",
         #"IITM-ESM",
         #"INM-CM4-8",
         #"INM-CM5-0",
         "IPSL-CM5A2-INCA",
         "IPSL-CM6A-LR",
         "IPSL-CM6A-LR-INCA",
         "KACE-1-0-G",
         #"KIOST-ESM",
         "MCM-UA-1-0",
         #"MIROC-ES2H",
         #"MIROC-ESM2L",
         #"MIROC6",
         "MPI-ESM-1-2-HAM",
         "MPI-ESM1-2-HR",
         "MPI-ESM1-2-LR",
         #"MRI-ESM2-0",
         "NESM3",
         #"NorCPM1",
         #"NorESM2-LM",
         #"NorESM2-MM",
         #"SAM0-UNICON",
         "TaiESM1",
         #"UKESM1-0-LL"
         ]

# models = ["UKESM1-0-LL"]
experiments = ["historical"]
frequency = "mon"
variables = ["siconc"]
variant = "r1i1p1f1"

for model in models:
    for exp in experiments:
        for var in variables:
            os.system(f"python cmip6_downloader.py --variable_id {var} --frequency {frequency} --experiment {exp} --source_id {model} --variant_label {variant}")
