import xarray as xr

outdir = './outputs/' #trailing /

def calc_blocks(model, prefix):
    files = []
    for i in range(2010,2040):
        files.append(prefix + str(i) + '.nc')
    ds = xr.open_mfdataset(files,concat_dim='dayofyear')
    dsmean = ds.mean('dayofyear')
    dsmean.to_netcdf(outdir + model + '_30yr_2010-2039.nc', mode='w', format='NETCDF4_CLASSIC')
    ds.close()

    files = []
    for i in range(2040,2070):
        files.append(prefix + str(i) + '.nc')
    ds = xr.open_mfdataset(files,concat_dim='dayofyear')
    dsmean = ds.mean('dayofyear')
    dsmean.to_netcdf(outdir + model + '_30yr_2040-2069.nc', mode='w', format='NETCDF4_CLASSIC')
    ds.close()


    files = []
    for i in range(2070,2100):
        files.append(prefix + str(i) + '.nc')
    ds = xr.open_mfdataset(files,concat_dim='dayofyear')
    dsmean = ds.mean('dayofyear')
    dsmean.to_netcdf(outdir + model + '_30yr_2070-2099.nc', mode='w', format='NETCDF4_CLASSIC')
    ds.close()

if __name__ == '__main__':
    calc_blocks('GFDL',outdir + 'corrected/min_GFDL-CM3_rcp85_')
    calc_blocks('NCAR',outdir + 'corrected/min_NCAR-CCSM4_rcp85_')
