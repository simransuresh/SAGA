import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import numpy as np
from matplotlib.animation import FuncAnimation
from time_reformat import time 

file_path = 'SAGA__SSHA_GEOVEL__60N_88N__2011_2020_rev_ext_alongtrack.nc'
ncfile = nc.Dataset(file_path, 'r')

sla = ncfile.variables['sla']
ug = ncfile.variables['ug']
vg = ncfile.variables['vg']
lat = ncfile.variables['lat'][:]
lon = ncfile.variables['lon'][:]
print(lon)

# fig, ax = plt.subplots(1, 1, figsize=(5, 3))

# m = Basemap(projection='npstere', lon_0=0, lat_0=90, boundinglat=60, ax=ax)
# x, y = m(lon, lat)

# def animate(frame):
#     m.pcolormesh(x, y, sla[frame,:,:], cmap='viridis', ax=ax)
#     m.colorbar(ax=ax, label='Sea level anomaly [m]')
#     ax.quiver(x, y, ug[frame,:,:], vg[frame,:,:], scale=10, color='black', alpha=0.5)
#     ax.set_title(time[frame])
#     return fig,

# animation = FuncAnimation(fig, animate, frames=len(time), interval=100) 

# m.drawcoastlines(ax=ax)
# ax.set_aspect('equal')
# plt.tight_layout()
# plt.show()

ncfile.close()

