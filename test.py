import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy import crs as ccrs
from plot_anim import lat, lon
from temp_mean import sla_annual_mean, ug_annual_mean, vg_annual_mean
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation

min_lat = 60
max_lat = 88
min_lon = -180
max_lon = 180
clon = (min_lon + max_lon) / 2
clat = (min_lat + max_lat) / 2
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
europe_bbox = [min_lon, max_lon, min_lat, max_lat]

fig, axs = plt.subplots(1, 1, figsize=(8,8), subplot_kw={'projection': ccrs.Orthographic(central_latitude=clat, central_longitude=clon)})
ax1 = axs
# ax2 = axs[1]
ax1.set_extent(europe_bbox, crs=ccrs.PlateCarree())
# ax2.set_extent(europe_bbox, crs=ccrs.PlateCarree())
world.boundary.plot(ax=ax1, linewidth=1, edgecolor='black', transform=ccrs.PlateCarree())
# world.boundary.plot(ax=ax2, linewidth=1, edgecolor='black', transform=ccrs.PlateCarree())
ax1.set_aspect('equal')
# ax2.set_aspect('equal')

m = Basemap(projection='npstere', lon_0=0, lat_0=90, boundinglat=60, ax=ax1)
x, y = m(lon, lat)
def animate1(frame):
    m.pcolormesh(x, y, sla_annual_mean[frame][:,:], cmap='viridis', ax=ax1)
    m.colorbar(ax=ax1, label='Sea level anomaly [m]')
    ax1.quiver(x, y, ug_annual_mean[frame][:,:], vg_annual_mean[frame][:,:], scale=10, color='black', alpha=0.5)
    ax1.set_title(frame)
    return fig,
animation1 = FuncAnimation(fig, animate1, frames=sla_annual_mean.keys(), interval=100) 

plt.show()




