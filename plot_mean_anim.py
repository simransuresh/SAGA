import matplotlib.pyplot as plt
from cartopy import crs as ccrs
from matplotlib.animation import FuncAnimation
import xarray as xr
import numpy as np
from read_sla_currents import lat, lon
from temporal_mean import sla_annual_mean, ug_annual_mean, vg_annual_mean, sla, ug, vg

############# plotting animation of annual mean of SLA, geostrophic currents
fig = plt.figure(figsize=(10, 8))
ax = plt.subplot(1, 1, 1, projection=ccrs.LambertAzimuthalEqualArea(central_longitude=0.0, central_latitude=80.0)) # LambertAzimuthalEqualArea / NorthPolarStereo
# ax = plt.subplot(1, 1, 1, projection=ccrs.NorthPolarStereo()) # LambertAzimuthalEqualArea / NorthPolarStereo
ax.coastlines(resolution='50m', linewidth=1)

# plot SLA with colorbar
im = ax.pcolormesh(lon, lat, sla_annual_mean[2011][:, :], transform=ccrs.PlateCarree(), cmap=plt.cm.seismic)
# im = ax.pcolormesh(lon, lat, sla[0, :, :], transform=ccrs.PlateCarree(), cmap=plt.cm.seismic)
cbar = plt.colorbar(im, ax=ax, orientation='vertical')
cbar.set_label('Sea Level Anomaly (m)')
im.set_clim(-1, 1)

# plot ug vg first time step using xarray quiver and subsampling resolution to reduce density
ds_velocity = xr.Dataset({'ug': (['lat', 'lon'], ug_annual_mean[2011]), 
                          'vg': (['lat', 'lon'], vg_annual_mean[2011])},
                         coords={'lon': lon[0,:], 'lat': lat[:,0]})
# ds_velocity = xr.Dataset({'ug': (['lat', 'lon'], ug[0,:,:]), 
                        #   'vg': (['lat', 'lon'], vg[0,:,:])},
                        #  coords={'lon': lon[0,:], 'lat': lat[:,0]})
ds_velocity.sel(lon=slice(None, None, 12), lat=slice(None, None, 4)).\
    plot.quiver('lon', 'lat', 'ug', 'vg', ax=ax, transform=ccrs.PlateCarree(), scale=1.5)

# animation function that updates each time step 
def update(frame):
    ax.clear()
    
    # update SLA 
    im = ax.pcolormesh(lon, lat, sla_annual_mean[frame][:, :], transform=ccrs.PlateCarree(), cmap=plt.cm.seismic)
    # im = ax.pcolormesh(lon, lat, sla[frame, :, :], transform=ccrs.PlateCarree(), cmap=plt.cm.seismic)
    ax.coastlines(resolution='50m', linewidth=1)
    # im.set_array(sla_annual_mean[frame].ravel())  # Update sla. after ax.clear removed it
    
    # update ug vg
    ds_velocity = xr.Dataset({'ug': (['lat', 'lon'], ug_annual_mean[frame].data), 
                          'vg': (['lat', 'lon'], vg_annual_mean[frame].data)},
                         coords={'lon': lon[0,:], 'lat': lat[:,0]})
    # ds_velocity = xr.Dataset({'ug': (['lat', 'lon'], ug[frame,:,:]), 
                        #   'vg': (['lat', 'lon'], vg[frame,:,:])},
                        #  coords={'lon': lon[0,:], 'lat': lat[:,0]})
    
    ds_velocity.sel(lon=slice(None, None, 12), lat=slice(None, None, 4)).\
    plot.quiver('lon', 'lat', 'ug', 'vg', ax=ax, transform=ccrs.PlateCarree(), scale=1.5)
    
    # show time step
    ax.set_title(frame)
    
    return im

# call animation function recursively
ani = FuncAnimation(fig, update, frames=sla_annual_mean.keys(), interval=200)
# ani = FuncAnimation(fig, update, frames=len(sla), interval=200)
plt.show()

####### why number 7.999.. appearing on the colorbar ??

####### plot time series of Barents Sea
# lat1 = 75.25
# lon1 = 37.5

# for i in range(2011, 2021):
    
#     plt.plot(i, ds_velocity.sel(lon=lon1, lat=lat1).values, 'r-')
# # ds_velocity.sel(lon=lon1, lat=lat1).plot('lon', 'lat', 'sla')
# plt.show()






