from read_sla_currents import lat, lon, mdt, temp_mean_sla, sla, ug, vg
import xarray as xr
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dot = mdt + sla + temp_mean_sla
print(dot.shape, mdt.shape)

# Generate a date range with monthly frequency
dtm = pd.date_range(start='2011-01-01', end='2020-12-31', freq='M')
print(dtm)

lats = np.array(lat[:,0])
lons = np.array(lon[0,:])

ds = xr.Dataset({'dot': (['time', 'lat', 'lon'], dot), 'ug': (['time', 'lat', 'lon'], ug), 'vg': (['time', 'lat', 'lon'], vg)}, 
                coords={'time': dtm, 'lon': lons, 'lat': lats})

# write monthly values for TPD and BG - month, dot, ug, vg

bg_lats = [70, 80]
bg_lons = [-175, -125]

# Select the subset of the dataset for the Beaufort Gyre region
subset = ds.sel(lat=slice(bg_lats[0], bg_lats[1]), lon=slice(bg_lons[0], bg_lons[1]))

# Now compute the spatial mean for each month This averages over the latitude and longitude dimensions
monthly_mean_beaufort_gyre = subset['dot'].mean(dim=['lat', 'lon'])

print(monthly_mean_beaufort_gyre)

plt.plot(dtm, monthly_mean_beaufort_gyre, linestyle='-', color='b', marker='o')

######## NO SEASONAL TRENDS FOUND SAME AS ANNUAL 
# # Group by time and filter summer months
# summer_data = subset.where(subset['time.month'].isin([12, 1, 2]), drop=True)
# annual_mean_gyre = monthly_mean_beaufort_gyre.resample(time='A').mean() # for annual
# # # Group by year (using 'time.year') and calculate the mean for each summer
# summer_mean_per_year = summer_data['dot'].groupby('time.year').mean(dim=['time', 'lat', 'lon'])
# # # Check the result
# print(summer_mean_per_year)
# # summer_mean_per_year.plot()
# plt.plot(list(range(2011, 2021)), summer_mean_per_year)
# plt.show()

# Convert the year and the data to numpy arrays for regression
years = pd.to_datetime(dtm).year + pd.to_datetime(dtm).dayofyear / 365.25
mean_values = monthly_mean_beaufort_gyre.values  # Extract the mean values

# Fit a linear trend using numpy.polyfit (1st degree polynomial for linear fit)
slope, intercept = np.polyfit(years, mean_values, 1)

# # Calculate the trend line values
trend_line = slope * years + intercept
print(slope)

plt.plot(dtm, trend_line, label=f'Trend (slope={slope:.4f})', linestyle='--', color='r')
plt.xlabel('Years')
plt.ylabel('Dynamic Height')
plt.title('Dynamic height of Beaufort gyre')
plt.legend()
plt.show()

# calculate percentage change
# Calculate the start and end years
start_year = years[0]  # First year in the time array
end_year = years[-1]  # Last year in the time array

# Calculate the initial dynamic height (at the start year)
initial_dynamic_height = slope * start_year + intercept

# Calculate the final dynamic height (at the end year)
final_dynamic_height = slope * end_year + intercept

# Calculate the change in dynamic height over the time period
change_in_dynamic_height = final_dynamic_height - initial_dynamic_height

# Calculate percentage change relative to the initial value
percentage_change = (change_in_dynamic_height / initial_dynamic_height) * 100
print(percentage_change)

# NOTE findings dh changed by 6.9% and 5.6% in monthly and annaul mean

# GSC
ug_beaufort_gyre = subset['ug'].mean(dim=['lat', 'lon'])*100
vg_beaufort_gyre = subset['vg'].mean(dim=['lat', 'lon'])*100

print(ug_beaufort_gyre, vg_beaufort_gyre)

plt.plot(dtm, ug_beaufort_gyre, linestyle='-', color='b', marker='o')
plt.plot(dtm, vg_beaufort_gyre, linestyle='-', color='g', marker='o')

years = pd.to_datetime(dtm).year + pd.to_datetime(dtm).dayofyear / 365.25
ug_values = ug_beaufort_gyre.values  # Extract the mean values
vg_values = vg_beaufort_gyre.values  # Extract the mean values

# Fit a linear trend using numpy.polyfit (1st degree polynomial for linear fit)
slope, intercept = np.polyfit(years, ug_values, 1)
slope2, intercept2 = np.polyfit(years, vg_values, 1)

# # Calculate the trend line values
trend_line = slope * years + intercept
trend_line2 = slope2 * years + intercept2
print(slope)

plt.plot(dtm, trend_line, label=f'Linear Trend (slope={slope:.4f})', linestyle='--', color='r')
plt.plot(dtm, trend_line2, label=f'Linear Trend (slope={slope2:.4f})', linestyle='--', color='r')
plt.xlabel('Years')
plt.ylabel('Geostrophic currents [cm/s]')
plt.title('Monthly mean of Geostrophic currents')
plt.legend()
plt.show()

start_year = years[0]  # First year in the time array
end_year = years[-1]  # Last year in the time array

# Calculate the initial dynamic height (at the start year)
initial_dynamic_height = slope * start_year + intercept

# Calculate the final dynamic height (at the end year)
final_dynamic_height = slope * end_year + intercept

# Calculate the change in dynamic height over the time period
change_in_dynamic_height = final_dynamic_height - initial_dynamic_height

# Calculate percentage change relative to the initial value
percentage_change = (change_in_dynamic_height / initial_dynamic_height) * 100
print(percentage_change)

## AO index
with open('data/AO_monthly_mean.txt', 'r+') as fp:
    ao_data = fp.readlines()
    
ao_data_to_plot = []

for idx in range(len(ao_data)):
    data = ao_data[idx][0:-1]
    ao_data_to_plot.append(float(data))
    
plt.plot(dtm, ao_data_to_plot, linestyle='-', color='b', marker='o')

plt.plot(dtm, 0 * years + 2, linestyle='--', color='r')
plt.plot(dtm, 0*years, linestyle='--', color='r')
plt.plot(dtm, 0 * years - 2, linestyle='--', color='r')
plt.xlabel('Years')
plt.ylabel('AO Index')
plt.title('Monthly mean of Arctic Oscillation Index')
# plt.legend()
plt.show()

# import netCDF4 as nc
file_path = 'data/monthly_20240926T0430.csv'


df = pd.read_csv(file_path, usecols=['ID', 'PARAM', 'Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 
                                     'Sep', 'Oct', 'Nov', 'Dec'])
print(df)