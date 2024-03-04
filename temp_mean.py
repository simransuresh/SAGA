'''
Calculates annual and biannual temporal mean fields of variables sla, ug, vg from SAGA
'''

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation
from plot_anim import lat, lon, time, ug, vg

############## load file 
file_path = 'SAGA__SSHA_GEOVEL__60N_88N__2011_2020_rev_ext_alongtrack.nc'
ncfile = nc.Dataset(file_path, 'r')

############## read variables
sla = ncfile.variables['sla']
ug = ncfile.variables['ug']
vg = ncfile.variables['vg']
print(sla.shape, ug.shape, vg.shape)

############## calculate annual mean
sla_annual_mean = {}
ug_annual_mean = {}
vg_annual_mean = {}
mon_idx = 0

for year_idx in range(2011, 2021):
    sla_annual_mean[year_idx] = np.mean(sla[mon_idx:mon_idx+12, :, :], axis=0)
    ug_annual_mean[year_idx] = np.mean(ug[mon_idx:mon_idx+12, :, :], axis=0)
    vg_annual_mean[year_idx] = np.mean(vg[mon_idx:mon_idx+12, :, :], axis=0)
    mon_idx += 12

print(sla_annual_mean[2020])
print(ug_annual_mean[2020])
print(vg_annual_mean[2020])


############## calculate biannual mean
sla_biannual_mean = {}
ug_biannual_mean = {}
vg_biannual_mean = {}
mon_idx = 0

for year_idx in range(2011, 2021, 2):
    print(f'{year_idx},{year_idx+1}')
    sla_biannual_mean[f'{year_idx},{year_idx+1}'] = np.mean(sla[mon_idx:mon_idx+24, :, :], axis=0)
    ug_biannual_mean[f'{year_idx},{year_idx+1}'] = np.mean(ug[mon_idx:mon_idx+24, :, :], axis=0)
    vg_biannual_mean[f'{year_idx},{year_idx+1}'] = np.mean(vg[mon_idx:mon_idx+24, :, :], axis=0)
    mon_idx += 24

print(sla_biannual_mean['2011,2012'])
print(ug_biannual_mean['2011,2012'])
print(vg_biannual_mean['2011,2012'])

############## plotting animation of annual mean
# fig, ax = plt.subplots(1, 2, figsize=(10, 8))

# m = Basemap(projection='npstere', lon_0=0, lat_0=90, boundinglat=60, ax=ax[0])
# x, y = m(lon, lat)
# def animate1(frame):
#     m.pcolormesh(x, y, sla_annual_mean[frame][:,:], cmap='viridis', ax=ax[0])
#     m.colorbar(ax=ax[0], label='Sea level anomaly [m]')
#     ax[0].quiver(x, y, ug_annual_mean[frame][:,:], vg_annual_mean[frame][:,:], scale=10, color='black', alpha=0.5)
#     ax[0].set_title(frame)
#     return fig,
# animation1 = FuncAnimation(fig, animate1, frames=sla_annual_mean.keys(), interval=100) 


############## plotting animation of biannual mean
# m = Basemap(projection='npstere', lon_0=0, lat_0=90, boundinglat=60, ax=ax[1])
# x, y = m(lon, lat)
# def animate2(frame):
#     m.pcolormesh(x, y, sla_biannual_mean[frame][:,:], cmap='viridis', ax=ax[1])
#     m.colorbar(ax=ax[1], label='Sea level anomaly [m]')
#     ax[1].quiver(x, y, ug_biannual_mean[frame][:,:], vg_biannual_mean[frame][:,:], scale=10, color='black', alpha=0.5)
#     ax[1].set_title(frame)
#     return fig,
# animation2 = FuncAnimation(fig, animate2, frames=sla_biannual_mean.keys(), interval=200) 

# m.drawcoastlines(ax=ax[0])
# m.drawcoastlines(ax=ax[1])
# ax[0].set_aspect('equal')
# ax[1].set_aspect('equal')
# # plt.tight_layout()
# plt.show()

