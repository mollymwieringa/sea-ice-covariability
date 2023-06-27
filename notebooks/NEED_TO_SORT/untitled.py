import xarray as xr
import numpy as np
import glob
import matplotlib.pyplot as plt
from matplotlib import colors
import datetime 

import scipy.signal as signal
import scipy.stats as stats
import statsmodels.api as sm


def read_historical_files(variable, cat): 
    dses = [] 
        
    cmip_dir1 = '/glade/collections/cmip/CMIP6/CMIP/NCAR/CESM2/historical/r1i1p1f1/'+cat+'/'+variable[0]+'/gn/files/d20190308/'
    files1 = glob.glob(cmip_dir1+variable[0]+'_'+cat+'_CESM2_historical_r1i1p1f1_gn_*[0-9]*')
    dses.append(xr.open_dataset(files1[0]))
        
    cmip_dir2 = '/glade/collections/cmip/CMIP6/CMIP/NCAR/CESM2/historical/r1i1p1f1/'+cat+'/'+variable[1]+'/gn/files/d20190308/'
    files2 = glob.glob(cmip_dir1+variable[1]+'_'+cat+'_CESM2_historical_r1i1p1f1_gn_*[0-9]*')
    dses.append(xr.open_dataset(files2[0]))
        
    cmip_ds = xr.concat(dses)
    
    # find volume 

    return cmip_ds

def read_CS2():
    file = '/glade/scratch/mollyw/external_data/CryoSat-2/YR_Cryosat-2/ubristol_cryosat2_seaicethickness_nh_80km_v1p7.nc'
    
    ds = xr.open_dataset(file, decode_times=False)
    
    no_days_0001 = ds.Time - 366
    
    time=[]
    for srl_no in no_days_0001.values:
        time.append(datetime.datetime(1,1,1,0,0) + datetime.timedelta(srl_no-1))
    
    
    ds['time'] = time
    ds = ds.drop("Time")
    
    ds["Sea_Ice_Volume"] = ds.Sea_Ice_Thickness * ds.Sea_Ice_Concentration

    return ds
    
def read_PIOMAS():
    files = sorted(glob.glob('/glade/scratch/mollyw/external_data/PIOMAS/daily/piomas_bin_reader/output/20*[0-9]*.nc'))
    ds_pms = xr.open_mfdataset(files, combine = 'nested', concat_dim = 'year')
    ds_pms = ds_pms.stack(time = ['year','t'])
    
    attrs = {'units': 'days since 2010-01-01'}
    time = xr.Dataset({'time': ('time', np.arange(0, len(ds_pms.time)), attrs)})
    time = xr.decode_cf(time)

    ds_pms["time"] = time.time
    ds_pms.rename({'thickness':'volume'})
    
    return ds_pms