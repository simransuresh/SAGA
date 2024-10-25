'''
Calculates annual and biannual temporal mean fields of variables sla, ug, vg from SAGA
'''

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid
from matplotlib.animation import FuncAnimation
from read_sla_currents import lat, lon, mdt, temp_mean_sla, sla, ug, vg

dot = mdt + sla + temp_mean_sla
print(dot.shape)

############## calculate annual mean
dot_annual_mean = {}
ug_annual_mean = {}
vg_annual_mean = {}
mon_idx = 0

for year_idx in range(2011, 2021):
    dot_annual_mean[year_idx] = np.mean(dot[mon_idx:mon_idx+12, :, :], axis=0)
    ug_annual_mean[year_idx] = np.mean(ug[mon_idx:mon_idx+12, :, :], axis=0)
    vg_annual_mean[year_idx] = np.mean(vg[mon_idx:mon_idx+12, :, :], axis=0)
    mon_idx += 12

############## calculate biannual mean
dot_biannual_mean = {}
ug_biannual_mean = {}
vg_biannual_mean = {}
mon_idx = 0

for year_idx in range(2011, 2021, 2):
    print(f'{year_idx},{year_idx+1}')
    dot_biannual_mean[f'{year_idx},{year_idx+1}'] = np.mean(dot[mon_idx:mon_idx+24, :, :], axis=0)
    ug_biannual_mean[f'{year_idx},{year_idx+1}'] = np.mean(ug[mon_idx:mon_idx+24, :, :], axis=0)
    vg_biannual_mean[f'{year_idx},{year_idx+1}'] = np.mean(vg[mon_idx:mon_idx+24, :, :], axis=0)
    mon_idx += 24

############## calculate total mean during 2011-2020
dot_mean = np.mean(dot[:, :, :], axis=0)
ug_mean = np.mean(ug[:, :, :], axis=0)
vg_mean = np.mean(vg[:, :, :], axis=0)

print(dot_mean.shape)
print(ug_mean.shape)
print(vg_mean.shape)

longitudes, latitudes = np.meshgrid(np.array(lon[0,:]), np.array(lat[:,0]))

# # ############# plotting animation of annual mean
# fig, axs = plt.subplots(1, 5, figsize=(8, 8))

# # 2011
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[0])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2011],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2011], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2011], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003) # TODO change scale=1.2, width=0.004
# qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '10 cm/s', labelpos='W') # TODO change this as well
# m.drawcoastlines(linewidth=1.5)

# # 2012
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[1])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2012],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2012], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2012], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)
    
# # 2013
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[2])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2013],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2013], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2013], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)

# # 2014
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[3])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2014],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2014], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2014], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)

# # 2015
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[4])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2015],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2015], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2015], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)

# # plt.savefig('annual_2011_2015_mean.png', dpi=300)

# fig, axs = plt.subplots(1, 5, figsize=(8, 8))

# # 2016
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[0])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2016],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2016], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2016], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)

# # 2017
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[1])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2017],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2017], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2017], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)
    
# # 2018
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[2])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2018],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2018], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2018], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)

# # 2019
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[3])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2019],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2019], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2019], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)

# # 2020
# m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[4])
# im = m.pcolormesh(longitudes,latitudes,dot_annual_mean[2020],cmap=plt.cm.YlGnBu, latlon=True)
# x, y = m(longitudes, latitudes)
# ugrid, newlons = shiftgrid(180., ug_annual_mean[2020], np.array(lon[0,:]), start=False)
# vgrid, newlons = shiftgrid(180., vg_annual_mean[2020], np.array(lon[0,:]), start=False)
# uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
# Q = m.quiver(xx, yy, uproj, vproj, scale=1.5, width=0.003)
# # qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '1 m/s', labelpos='W')
# m.drawcoastlines(linewidth=1.5)

# # colorbar
# cax = fig.add_axes([0.27, 0.35, 0.5, 0.03])
# cbar = fig.colorbar(im, orientation='horizontal', cax=cax)
# cbar.set_label('DOT (m)')
# im.set_clim(0, 0.8)

# fig.tight_layout()
# # plt.subplots_adjust(wspace=None, hspace=None)
# # plt.savefig('annual_2016_2020_mean.png', dpi=300)
# # plt.show()

####### plot of biannual mean
fig, axs = plt.subplots(1, 5, figsize=(8, 8))

# 2011, 2012
m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[0])
im = m.pcolormesh(longitudes,latitudes,dot_biannual_mean['2011,2012'],cmap=plt.cm.YlGnBu, latlon=True)
x, y = m(longitudes, latitudes)
ugrid, newlons = shiftgrid(180., ug_biannual_mean['2011,2012'], np.array(lon[0,:]), start=False)
vgrid, newlons = shiftgrid(180., vg_biannual_mean['2011,2012'], np.array(lon[0,:]), start=False)
uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
Q = m.quiver(xx, yy, uproj, vproj, scale=1.2, width=0.004)
m.drawcoastlines(linewidth=1.5)
axs[0].set_title('2011,2012')

# 2013, 2014
m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[1])
im = m.pcolormesh(longitudes,latitudes,dot_biannual_mean['2013,2014'],cmap=plt.cm.YlGnBu, latlon=True)
x, y = m(longitudes, latitudes)
ugrid, newlons = shiftgrid(180., ug_biannual_mean['2013,2014'], np.array(lon[0,:]), start=False)
vgrid, newlons = shiftgrid(180., vg_biannual_mean['2013,2014'], np.array(lon[0,:]), start=False)
uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
Q = m.quiver(xx, yy, uproj, vproj, scale=1.2, width=0.004)
m.drawcoastlines(linewidth=1.5)
axs[1].set_title('2013,2014')

# 2015, 2016
m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[2])
im = m.pcolormesh(longitudes,latitudes,dot_biannual_mean['2015,2016'],cmap=plt.cm.YlGnBu, latlon=True)
x, y = m(longitudes, latitudes)
ugrid, newlons = shiftgrid(180., ug_biannual_mean['2015,2016'], np.array(lon[0,:]), start=False)
vgrid, newlons = shiftgrid(180., vg_biannual_mean['2015,2016'], np.array(lon[0,:]), start=False)
uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
Q = m.quiver(xx, yy, uproj, vproj, scale=1.2, width=0.004)
m.drawcoastlines(linewidth=1.5)
axs[2].set_title('2015,2016')

# 2017, 2018
m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[3])
im = m.pcolormesh(longitudes,latitudes,dot_biannual_mean['2017,2018'],cmap=plt.cm.YlGnBu, latlon=True)
x, y = m(longitudes, latitudes)
ugrid, newlons = shiftgrid(180., ug_biannual_mean['2017,2018'], np.array(lon[0,:]), start=False)
vgrid, newlons = shiftgrid(180., vg_biannual_mean['2017,2018'], np.array(lon[0,:]), start=False)
uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
Q = m.quiver(xx, yy, uproj, vproj, scale=1.2, width=0.004)
m.drawcoastlines(linewidth=1.5)
axs[3].set_title('2017,2018')

# 2019, 2020
m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, round=True, ax=axs[4])
im = m.pcolormesh(longitudes,latitudes,dot_biannual_mean['2019,2020'],cmap=plt.cm.YlGnBu, latlon=True)
x, y = m(longitudes, latitudes)
ugrid, newlons = shiftgrid(180., ug_biannual_mean['2019,2020'], np.array(lon[0,:]), start=False)
vgrid, newlons = shiftgrid(180., vg_biannual_mean['2019,2020'], np.array(lon[0,:]), start=False)
uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, np.array(lat[:,0]), 32, 32, returnxy=True, masked=True)
Q = m.quiver(xx, yy, uproj, vproj, scale=1.2, width=0.004)
m.drawcoastlines(linewidth=1.5)
axs[4].set_title('2019,2020')

# colorbar
cax = fig.add_axes([0.27, 0.35, 0.5, 0.03])
cbar = fig.colorbar(im, orientation='horizontal', cax=cax)
cbar.set_label('DOT (m)')
im.set_clim(0, 0.8)

fig.tight_layout()
plt.show()
# plt.savefig('biannual_mean.png', dpi=300)