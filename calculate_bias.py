import xarray as xr

inputdir = '/atlas_scratch/apbennett/wrfdata/t2/' #trailing /
outdir = './outputs/' #trailing /

print('Beginning ERA')
fileprefix = inputdir + 't2min_daily_wrf_ERA-Interim_historical_'
files = []
for i in range(1980,2010):
    year = i
    files.append(fileprefix + str(year) + '.nc')

era = xr.open_mfdataset(files)
era_noleap = era.sel(time=~((era.time.dt.month == 2) & (era.time.dt.day == 29)))
era_daymean = era_noleap.groupby("time.dayofyear").mean(dim='time') - 273.15
filename = outdir + '30yr_min_mean_ERA_1980-2009.nc'
era_daymean.to_netcdf(filename, mode='w', format='NETCDF4_CLASSIC')
era.close()

print('Beginning NCAR')
fileprefix = inputdir + 't2min_daily_wrf_NCAR-CCSM4_historical_'
files = []
for i in range(1980,2006):
    files.append(fileprefix + str(i) + '.nc')

fileprefix = inputdir + 't2min_daily_wrf_NCAR-CCSM4_rcp85_'
for i in range(2006,2010):
    files.append(fileprefix + str(i) + '.nc')

ncar = xr.open_mfdataset(files)
ncar_noleap = ncar.sel(time=~((ncar.time.dt.month == 2) & (ncar.time.dt.day == 29)))
ncar_daymean = ncar_noleap.groupby("time.dayofyear").mean(dim='time') - 273.15
filename = outdir + '30yr_min_mean_NCAR_1980-2009.nc'
ncar_daymean.to_netcdf(filename, mode='w', format='NETCDF4_CLASSIC')
ncar.close()

print('Beginning GFDL')
fileprefix = inputdir + 't2min_daily_wrf_GFDL-CM3_historical_'
files = []
for i in range(1980,2006):
    files.append(fileprefix + str(i) + '.nc')

fileprefix = inputdir + 't2min_daily_wrf_GFDL-CM3_rcp85_'
for i in range(2006,2010):
    files.append(fileprefix + str(i) + '.nc')

gdal = xr.open_mfdataset(files)
gdal_noleap = gdal.sel(time=~((gdal.time.dt.month == 2) & (gdal.time.dt.day == 29)))
gdal_daymean = gdal_noleap.groupby("time.dayofyear").mean(dim='time') - 273.15
filename = outdir + '30yr_min_mean_GFDL_1980-2009.nc'
gdal_daymean.to_netcdf(filename, mode='w', format='NETCDF4_CLASSIC')
gdal.close()
files = []

print('Calculating NCAR Bias')
ncar_bias = ncar_daymean - era_daymean
ncar_bias.to_netcdf(outdir + 'NCAR_Bias_1980-2009.nc', mode='w', format='NETCDF4_CLASSIC')
print('Calculating GFDL Bias')
gdal_bias = gdal_daymean - era_daymean
gdal_bias.to_netcdf(outdir + 'GFDL_Bias_1980-2009.nc', mode='w', format='NETCDF4_CLASSIC')
print('Bias Calculation Complete')
