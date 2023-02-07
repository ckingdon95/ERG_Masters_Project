# Define multiple ucnertainty metrics.
# Each metric is defined for one grid cell, some computation across available simulations.


def max_diff(da):
    """
    Absolute difference between the max and min simulation values at each
    grid cell.
    """
    return da.max(dim='simulation') - da.min(dim='simulation')

def max_diff_pct(da):
    """
    Percent difference between the max and min simulation values at each grid
    cell.
    """
    return (da.max(dim='simulation') - da.min(dim='simulation')) / da.min(dim='simulation')

def max_diff_mean(da):
    """
    Absolute difference between the max and min simulation values divided by 
    the mean at each grid cell.
    """
    return (da.max(dim='simulation') - da.min(dim='simulation')) / da.mean(dim='simulation')

def cv(da):
    """
    Coefficient of variation across simulations. Standard deviation devided by
    the mean across simulations at each grid cell.
    """
    return da.std(dim='simulation') / da.mean(dim='simulation')


#------------------ Extreme event definitions

# Hottest hour per year
# Hottest continuous 3-days
# Number of days above 95
# Number of days above present-day hottest day of year

# average over ten years
# return value (1-in-20 year value)