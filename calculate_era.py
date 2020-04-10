import xarray as xr

inputdir = '/atlas_scratch/apbennett/wrfdata/t2/' #trailing /
outdir = './outputs/'

for i in range(1980,2010):
    print('Calculating ERA Mins ' + str(i))
    fileprefix = inputdir + 't2min_daily_wrf_ERA-Interim_historical_'
    era_annual = xr.open_dataset(fileprefix + str(i) + '.nc') - 273.15
    era_min = era_annual.min('time')
    era_min.to_netcdf(outdir + 'corrected/min_ERA_' + str(i) + '.nc', mode='w', format='NETCDF4_CLASSIC')
    era_annual.close()

files = []
for i in range(1980,2010):
    fileprefix = outdir + 'corrected/min_ERA_'
    files.append(fileprefix + str(i) + '.nc')

ds = xr.open_mfdataset(files,concat_dim='time')
ds_mean = ds.mean('time')
ds_mean.to_netcdf(outdir + 'ERA_30yr.nc', mode='w', format='NETCDF4_CLASSIC')
