import xarray as xr
import matplotlib.pyplot as plt

# Open the dataset
data = xr.open_dataarray("./t2m_era_China_clim2010-2013.nc")

# plot timeseries of some arbitrary latitudes and longitudes
data.isel(latitude=10, longitude=10).plot()
data.isel(latitude=13, longitude=8).plot(label='for the legend')

# Add a legend
plt.legend()

# Show this plot (if not running interactively on the command line)
plt.show()