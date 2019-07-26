import xarray as xr
import matplotlib.pyplot as plt

# Open the dataset
data = xr.open_dataarray("./t2m_era_China_clim2010-2013.nc")

# Find the temperature range for each point over the year
range = data.max(dim='time') - data.min(dim='time')

# plot on a map
range.plot()

# Show this plot (if not running interactively on the command line)
plt.show()