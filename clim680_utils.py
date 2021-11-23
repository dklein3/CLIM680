import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
from cartopy.util import add_cyclic_point

def latlonticks(ax,lon_min=-180,lon_max=181,lon_int=60,lat_min=-90,lat_max=91,lat_int=30):
    """
    This function produces map ticks on your plot with default values of...
    """
    # Define the xticks for longtitude 
    ax.set_xticks(np.arange(lon_min,lon_max,lon_int),crs=ccrs.PlateCarree())
    lon_formatter=cticker.LongitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)

    # Define ytick for latitude
    ax.set_yticks(np.arange(lat_min,lat_max,lat_int),crs=ccrs.PlateCarree())
    lat_formatter=cticker.LatitudeFormatter()
    ax.yaxis.set_major_formatter(lat_formatter)
    
    return
