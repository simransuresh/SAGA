import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import numpy as np
import geopandas as gpd
from time_reformat import time 

file_path = 'SAGA__SSHA_GEOVEL__60N_88N__2011_2020_rev_ext_alongtrack.nc'
ncfile = nc.Dataset(file_path, 'r')

sla = ncfile.variables['sla'][0, :, :]
ug = ncfile.variables['ug'][0, :, :]
vg = ncfile.variables['vg'][0, :, :]
lat = ncfile.variables['lat'][:]
lon = ncfile.variables['lon'][:]
print(time)

fig, ax = plt.subplots(1, 1, figsize=(15, 5))
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# world.boundary.plot(ax=ax1, linewidth=1, edgecolor='black', transform=ccrs.PlateCarree())

m = Basemap(projection='npstere', lon_0=0, lat_0=90, boundinglat=60, ax=ax)
x, y = m(lon, lat)

m.pcolormesh(x, y, sla, cmap='viridis', ax=ax)
m.colorbar(ax=ax)
ax.quiver(x, y, ug, vg, scale=10, color='red', alpha=0.5)

m.drawcoastlines(ax=ax)
# ax.coastlines(color="0.1")
# ax.set_title(f'{sla.name} [m]')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_aspect('equal')
plt.tight_layout()
plt.show()

ncfile.close()

