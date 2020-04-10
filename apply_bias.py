import xarray as xr

inputdir = '/atlas_scratch/apbennett/wrfdata/t2/'
outdir = './outputs/'

ncar_bias = xr.open_dataset(outdir + 'NCAR_Bias_1980-2009.nc')
gfdl_bias = xr.open_dataset(outdir + 'GFDL_Bias_1980-2009.nc')

for i in range(2010,2100):
    print('Applying NCAR Bias to ' + str(i))
    fileprefix = inputdir + 't2min_daily_wrf_NCAR-CCSM4_rcp85_'
    ncar_annual = xr.open_dataset(fileprefix + str(i) + '.nc') - 273.15
    ncar_annual_noleap = ncar_annual.sel(time=~((ncar_annual.time.dt.month == 2) & (ncar_annual.time.dt.day == 29)))
    ncar_annual_daymean = ncar_annual_noleap.groupby("time.dayofyear").mean(dim='time')
    ncar_corrected = ncar_annual_daymean + ncar_bias
    ncar_min = ncar_corrected.min('dayofyear')
    ncar_min.to_netcdf(outdir + 'corrected/min_NCAR-CCSM4_rcp85_' + str(i) + '.nc', mode='w', format='NETCDF4_CLASSIC')
    ncar_annual.close()
    ncar_corrected.close()
    
    print('Applying GFDL Bias to ' + str(i))
    fileprefix = inputdir + 't2min_daily_wrf_GFDL-CM3_rcp85_'
    gfdl_annual = xr.open_dataset(fileprefix + str(i) + '.nc') - 273.15
    gfdl_annual_noleap = gfdl_annual.sel(time=~((gfdl_annual.time.dt.month == 2) & (gfdl_annual.time.dt.day == 29)))
    gfdl_annual_daymean = gfdl_annual_noleap.groupby("time.dayofyear").mean(dim='time')
    gfdl_corrected = gfdl_annual_daymean + gfdl_bias
    gfdl_min = gfdl_corrected.min('dayofyear')
    gfdl_min.to_netcdf(outdir + 'corrected/min_GFDL-CM3_rcp85_' + str(i) + '.nc', mode='w', format='NETCDF4_CLASSIC')
    gfdl_annual.close()
    gfdl_corrected.close()
