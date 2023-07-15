#!/usr/bin/env python
# coding: utf-8

# # Plot Precipitation
# 
# <h1>Winter (Dec-Jan-Feb) averaged precipitation in the 50 member CESM2 large ensemble</h1>
# 
# <h2>In this notebook you'll read in data from 50 members of the CESM2 large ensemble and explore the climate change response and the uncertainty due to internal variability in the winter means of precipitation</h2>

# <h3><font color='red'>Cell 1</font></h3>

# In[ ]:


# Execute this cell to load the functions necessary for the computations
from functions import *
import xarray as xr
import matplotlib.pyplot as plt
from math import nan
import warnings
warnings.filterwarnings('ignore')


# <h3>Execute the cell below to read in the data</h3>

# <h3><font color='red'>Cell 2</font></h3>

# In[ ]:


# Model ensemble
pr = xr.open_dataset("/scratch/data/DATA4LENS2/output_lens2_djf/PR/PR_djf_LENS2_second50.nc")
pr['time'] = pr.time.dt.year
# Observations
obs = xr.open_dataset("/scratch/data/DATA4LENS2/output_obs/GPCC_precip.nc")
obs['time'] = obs.time.dt.year


# <h3>We'll look again at the projected change of the average of 10 winters and compare relative to the 10 winters from 1980-1989.  Feel free to change start_year_of_decade to a different value to explore the model's forced climate change response (you won't see any observations of the future)</h3>

# <h3><font color='red'>Cell 3</font></h3>

# In[ ]:


start_year_of_decade = 2080
print("You're now going to look at the decade from "+str(start_year_of_decade)+" to "+str(start_year_of_decade+9))

fig = plt.figure(figsize=(16,16))

fig = plot_prmap_ensemblemean(fig, obs, pr, start_year_of_decade)


# ### Here you can plot the individual members from the ensemble.  Feel free to modify the members that are plotted by changing the numbers in the members array.  Note that you can only have a maximum of 9 members

# <h3><font color='red'>Cell 4</font></h3>

# In[ ]:


fig = plt.figure(figsize=(16,16))

members=[1,2,3,4,5,6,7,8,9]
fig = plot_prmap_members(fig, obs, pr, start_year_of_decade, members)


# In[ ]:




