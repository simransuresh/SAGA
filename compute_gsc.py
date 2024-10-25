import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from read_sla_currents import sla, lat, lon, ug, vg, mdt, temp_mean_sla
from dayssince2utc import time
from cartopy import crs as ccrs
import math

############## assumptions
# let 'x' be lon or phi, 'y' be lat or theta
dot = mdt + sla + temp_mean_sla
dot = np.mean(dot, axis=0)
ug = np.mean(ug, axis=0)
vg = np.mean(vg, axis=0)

############## constants
g = 9.81 # 9.832 / 9.81 m/s2
Re = 6371008 # 6399593.6259 / 6371008 m

############## dataset
lats = np.array(lat[:,0])
lons = np.array(lon[0,:])
# print(lats, lons)

ds = xr.Dataset({'dot': (['lat', 'lon'], dot), 'mdt': (['lat', 'lon'], mdt), 'ug': (['lat', 'lon'], ug), 'vg': (['lat', 'lon'], vg)}, 
                coords={'lon': lons, 'lat': lats})

# test values from dataset
print(ds.sel(lat=78.75, lon=-150.75)['dot'].values)
print(ds.sel(lat=78.75, lon=-150.75)['mdt'].values)
print(ds.sel(lat=78.75, lon=-150.75)['ug'].values)
print(ds.sel(lat=78.75, lon=-150.75)['vg'].values)

# testing with PS144 station 6 data
print(ds.sel(lat=85, lon=42.5, method='nearest')['dot'].values)
print(ds.sel(lat=85, lon=42.5, method='nearest')['mdt'].values)
ug = ds.sel(lat=85, lon=42.5, method='nearest')['ug'].values
vg = ds.sel(lat=85, lon=42.5, method='nearest')['vg'].values
print(ug, vg)

############# compute geostrophic currents from ssh
# ug = -(g / (f * Re)) * (∂xη / ∂y)
# vg = (g / (f * Re) cos(y)) * (∂η / ∂x)

# print('Computing Geostrophic currents from SLA/DOT.....')

# Coriolis parameter
# f = 2 * 7.29e-5 * np.sin(np.deg2rad(lats[:, np.newaxis]))
# print(f)

# # Compute gradients using central differences
# ddot_dx = np.zeros(lon.shape)
# ddot_dy = np.zeros(lat.shape)

# lat_idx= 0
# lon_idx = 0
# lat_res = 0.25
# lon_res = 0.75

# # wrt longitude along x
# for lat in np.arange(60, 88.25, lat_res):
#     ddot_dx[lat_idx, 1:-1] = [(ds.sel(lat=lat, lon=lon+lon_res)['dot'] - ds.sel(lat=lat, lon=lon-lon_res)['dot']) / (np.deg2rad(lon+lon_res)-np.deg2rad(lon-lon_res)) for lon in np.arange(-178.5, 180, lon_res)]
#     lat_idx += 1
    
# # wrt latitude along y
# for lon in np.arange(-179.25, 180.75, 0.75):
#     ddot_dy[1:-1, lon_idx] = [(ds.sel(lat=lat+lat_res, lon=lon)['dot'] - ds.sel(lat=lat-lat_res, lon=lon)['dot']) / (np.deg2rad(lat+lat_res)-np.deg2rad(lat-lat_res)) for lat in np.arange(60.25, 88, lat_res)]
#     lon_idx += 1
    
# print(ddot_dx.shape, ddot_dy.shape) 

# # Compute geostrophic currents
# nug = -(g / (f*Re)) * ddot_dy 
# nvg = (g / (f*Re*np.cos(np.deg2rad(lats[:, np.newaxis])))) * ddot_dx 

# # computed values as new dataset
# nds = xr.Dataset({'dot': (['lat', 'lon'], dot), 'ug': (['lat', 'lon'], nug), 'vg': (['lat', 'lon'], nvg)}, coords={'lon': lons, 'lat': lats})

# # validate with test values
# print(nds.sel(lat=79.25, lon=0.75)['dot'].values)
# print(nds.sel(lat=79.25, lon=0.75)['ug'].values)
# print(nds.sel(lat=79.25, lon=0.75)['vg'].values)

## OLD
########### Quiver plot of computed ug and vg
# fig = plt.figure(figsize=(10, 8))
# ax = plt.subplot(1, 1, 1, projection=ccrs.NorthPolarStereo()) # LambertAzimuthalEqualArea / NorthPolarStereo
# ax.coastlines(resolution='50m', linewidth=1)

# # plot DOT with colorbar
# im = ax.pcolormesh(lons, lats, dot, transform=ccrs.PlateCarree(), cmap=plt.cm.seismic)
# cbar = plt.colorbar(im, ax=ax, orientation='vertical')
# cbar.set_label('DOT (m)')
# im.set_clim(-0.5, 0.5)

# nds.sel(lon=slice(None, None, 12), lat=slice(None, None, 5)).plot.quiver('lon', 'lat', 'ug', 'vg', ax=ax, transform=ccrs.PlateCarree(), scale=1.5)
# plt.show()

