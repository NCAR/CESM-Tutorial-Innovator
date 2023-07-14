#!/usr/bin/env python
# coding: utf-8

# # Customize CLM output
# 
# In this section, we will cover:
# - how to change the **output frequency**
# - how to control the **number of time samples** written to a history file
# - how to output **extra variables**
# - how to output **extra history files**
# 
# This can be achieved with 3 namelist variables:
# - **``hist_nhtfrq:``**: output frequency of the history file 
# - **``hist_mfilt``**: number of samples on each history file
# - **``hist_fincl``**: adding variables and auxiliary history files

# ## Customizing CLM output frequency: **``hist_nhtfrq``**
# We can change the output frequency with the namelist variable **``hist_nhtfrq``**
# - If **``hist_nhtfrq=0``**, the file will be a **monthly** average
# - If **``hist_nhtfrq>0``**, frequency is input as number of **timesteps**.
# - If **``hist_nhtfrq<0``**, frequency is input as number of **hours**.
# 
# For instance, 
# 
# ```
#      hist_nhtfrq = -24
# ```
# means **daily output**
# 
# ```
#      hist_nhtfrq = 24
# ```
# means output every **24 timesteps**
# 
# 
# <div class="alert alert-info">
# <strong>Evaluate your understanding</strong>
# 
# How do you modify the CLM output to output 3-hourly data ? 
# 
# </div>
# 
# <div class="alert alert-success">
#    
# <details>   
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
# 
# Add the following line to <font face="Courier"><strong>user_nl_clm</strong></font>:<br>
# ```
#     hist_nhtfrq = -3
# ```
# 
# </details>
# </div>

# 
# ## Add extra variables and history files: **``hist_fincl``**
# 
# You can output up to 10 history files:**``h0``**, **``h1``**, …, **``h9``**. 
# 
# To control the list of fields in the history files, use the namelist variable **``hist_fincl``**
# - **``hist_fincl1``** controls the fields in **``h0``** 
# - **``hist_fincl2``** controls the fields in **``h1``** 
# - ...
# - **``hist_fincl10``** controls the fields in **``h9``** 
# 
# For example, to add the field 'TG' to the ``h0`` file, use the line:
# ```
#      hist_fincl1 = 'TG' 
# ```
# 
# <div class="alert alert-info">
# <strong>Evaluate your understanding</strong>
# 
# What is the namelist setting to add a monthly history h1 with the variables 'TG', 'TV' and a daily history h2 with the variables 'TG', 'TV'. Output 10 time samples in h1 and h2 ? 
# </div>
# 
# <div class="alert alert-success">  
# <details>  
# 
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
# 
# Modify <font face="Courier"><strong>env_run.xml</strong></font> with the command:
# ``` 
#     ./xmlchange STOP_N=nmonths, STOP_OPTION=1
# ```
# 
# Add the following lines to <font face="Courier"><strong>user_nl_cam</strong></font>:
# ``` 
#     hist_nhtfrq = 0, 0, -24 
#     hist_mfilt = 1, 10, 10 
#     hist_fincl2 = 'TG', 'TV' 
#     hist_fincl3 = 'TG', 'TV' 
# ```
# 
# </details>
# </div>
# 
# 

# ## Customizing CLM history files: **``hist_mfilt``**
# To control the number of time samples in the history file, we use the variable **``hist_mfilt``**. <br>
# This variable specifies is the maximum number of time samples written to a history file.
# 
# For example, if we want to have **10 time samples** on each history file, we can set the namelist variable as follows:
# ```
#      hist_mfilt = 10
# ```
# 
# 
# To output **daily** data in a single file for a 1-year run, we can use the following values:
# ```
#     hist_nhtfrq = -24   
#     hist_mfilt = 365
# ```
# If we want to output **daily** data with only **1 time sample** per file, we can set the variables as follows:
# ```
#     hist_nhtfrq = -24
#     hist_mfilt = 1
# ```
# 
# NB: we cannot change mfilt for monthly frequency. 	For monthly frequency, we always have: 
# ```hist_mfilt = 1``` 
# 
# <div class="alert alert-info">
# <strong>Evaluate your understanding</strong>
# 
# What is the setting to generate CLM 3-hourly data for a month-long simulation that will create a file every day?
# 
# </div>
# 
# <div class="alert alert-success">  
# <details>  
# 
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
# 
# Modify <font face="Courier"><strong>env_run.xml</strong></font> with the command:
# ```
#     ./xmlchange STOP_N=nmonths, STOP_OPTION=1
# ```
# 
# Add the following line to <font face="Courier"><strong>user_nl_cam</strong></font>:
# ``` 
#     hist_nhtfrq = -3
#     hist_mfilt = 8
# ```
# 
# </details>
# </div>
# 
# 

# 
# ## Averaging flag for the **``fincl``** variables 
# 
# Using a ":" following a field gives the averaging flag for the output field. 
# 
# Valid flags are: 
# - **``A``** ==> Average
# - **``I``** ==> Instantaneous
# - **``M``** ==> Minimum
# - **``X``** ==> Maximum
# - **``SUM``** ==> Sum
# 
# For instance, the line:
# ```
#      hist_fincl1  = 'TLAI:M' 
# ```
# is used to add the minimum of ``TLAI`` to the file ``h0``
# 
# 
# 
# 

# 
# <div class="alert alert-info">
# <strong>Evaluate your understanding</strong>
# 
# What happens if we set in <font face="Courier"><strong>user_nl_clm</strong></font>:
# ```
#     hist_fincl2 = 'TG', 'TV' 
#     hist_fincl3 = 'TG', 'TV' 
#     hist_fincl4 = 'TG', 'TV'
#     hist_fincl5 = 'TG', 'TV' 
#     hist_nhtfrq = 0, -24, -6, -1, 1 
# ```
# 
# </div>
# 
# <div class="alert alert-success">  
# <details>  
# 
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
# 
# In addition to the monthly history file <strong>h0</strong>, we output 4 extra history files with daily, six-hourly, hourly, and every time-step values of TG and TV (leaving the primary history ``h0`` files as monthly). 
# 
# </details>
# </div>

# In[ ]:




