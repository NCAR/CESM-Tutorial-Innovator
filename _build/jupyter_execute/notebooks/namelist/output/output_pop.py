#!/usr/bin/env python
# coding: utf-8

# # Customize POP output
# 
# POP output is controlled by POP's tavg_nml namelist, which variables such as
# 
# - **``tavg_freq``**: frequency at which the model fields are written
# - **``tavg_freq_opt``**: units of time for 'tavg_freq’ ('nmonth’, 'nhour’, 'once’,…)
# - **``tavg_file_freq``**:frequency at which the model files are written
# - **``tavg_file_freq_opt``**: units of time for 'tavg_file_freq’ ('nmonth’, 'nhour’, …)
# 
# These are arrays, with a value for each output stream.
# A convenient way to change the first stream to be daily averages bundled into monthly
# files is to add the following lines to ``user_nl_pop``: 
# ```
# tavg_freq_opt(1) = 'nday' 
# tavg_freq(1) = 1 
# tavg_file_freq_opt(1) = 'nmonth' 
# tavg_file_freq(1) = 1 
# ```
# 
# See: https://www.cesm.ucar.edu/models/cesm2/settings/current/pop2_nml.html
# 
# 
# CAUTION: Note that changing tavg_nml variables via ``user_nl_pop`` is non-standard.
# While the above is convenient, attempting more complicated changes can lead to unexpected model behavior.
# For full flexibility, use the **workaround** explained in ``user_nl_pop``.
# 

# In[ ]:




