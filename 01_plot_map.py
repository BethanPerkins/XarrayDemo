import xarray as xr
import matplotlib.pyplot as plt # not needed on the command line

# Open the dataset
data = xr.open_dataarray("./t2m_era_China_clim2010-2013.nc")

# Look at the attributes
print(data)

# plot a map of the first timestep
data.isel(time=0).plot()

# Show this plot (if not running interactively on the command line)
plt.show()