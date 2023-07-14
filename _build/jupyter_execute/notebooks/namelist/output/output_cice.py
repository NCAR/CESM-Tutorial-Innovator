#!/usr/bin/env python
# coding: utf-8

# # Customize CICE output
# 
# The CICE output can changed with the namelist variables
# 
# - **``histfreq``**: Frequency of output written to history files ('1', 'm', 'd', 'y', …)
# - **``histfreq_n``**: Frequency history data is written to history files
# - **``hist_avg``**: if false => instantaneous values, if true => time-averages
# 
# 
# Here is how to set ``user_nl_cice`` to output an extra history file with daily values (leaving the primary history file as monthly): 
# ```
#      histfreq = 'm','d','x','x','x'
#      histfreq_n = 1,1,1,1,1 
# ```
# 
# See: http://www.cesm.ucar.edu/models/cesm2/settings/current/cice_nml.html
# 
# 

# In[ ]:




