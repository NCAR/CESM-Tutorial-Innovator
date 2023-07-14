#!/usr/bin/env python
# coding: utf-8

# # Customize CAM output
# 
# In this section, we will cover:
# - how to change the **output frequency**
# - how to control the **number of time samples** written to a history file
# - how to output **extra variables**
# - how to output **extra history files**
# 
# This can be achieved with 3 namelist variables:
# - **``nhtfrq``**: sets the output frequency
# - **``mfilt``**: maximum number of time samples written to a history file
# - **``fincl``**: add variables to the history file
# 
# 

# ## Customizing CAM output frequency: **``nhtfrq``**
# The default history file from CAM is a monthly average. 
# We can change the **output frequency** with the namelist variable **``nhtfrq``**
# - If **``nhtfrq=0``**, the file will be a **monthly** average
# - If **``nhtfrq>0``**, frequency is input as number of **timesteps**.
# - If **``nhtfrq<0``**, frequency is input as number of **hours**.
# 
# For instance to change the history file from monthly average to daily average, we set the namelist variable:
# 
# ```
#     nhtfrq = -24     
# ```
# 
# 
# <div class="alert alert-info">
# <strong>Evaluate your understanding</strong>
# 
# The default history file in CAM is a monthly average. How do you modify the output to output 3-hourly data ? 
# 
# </div>
# 
# <div class="alert alert-success">
#    
# <details>   
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
# Add the following line to <font face="Courier"><strong>user_nl_cam</strong></font>:<br>
# 
# ```
#     nhtfrq = -3
# ```
# </details>
# </div>

# ## Customizing CAM history files: **``mfilt``**
# To control the **number of time samples** in the history file, we use the variable **``mfilt``**. <br>
# This variable specifies is the maximum number of time samples written to a history file.
# 
# For example, if we want to have 10 time samples on each history file, we can set the namelist variable as follows:
# ```
#      mfilt = 10
# ```
# 
# 
# To output daily data for a 1-year run in a single file, we can use the following values:
# ```
#     nhtfrq = -24   
#     mfilt = 365
# ```
# If we want to output daily data with only 1 time sample per file, we can set the variables as follows:
# ```
#     nhtfrq = -24
#     mfilt = 1
# ```
# 
# NB: we cannot change mfilt for monthly frequency. For monthly frequency, we always have: 
# ```mfilt = 1``` 
# 
# <div class="alert alert-info">
# <strong>Evaluate your understanding</strong>
# 
# What is the setting to generate 3 hourly data for a month-long simulation that will create a file every day? 
# </div>
# 
# <div class="alert alert-success">  
# <details>  
# 
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
# 
# Modify the length of the run in `env_run.xml` with the command:
# ```    
#     ./xmlchange STOP_N=nmonths, STOP_OPTION=1
# ```
# 
# Add the following line to `user_nl_cam` to output 3 hourly data and to create one file per day:
# ```  
#     nhtfrq = -3
#     mfilt = 8
# ```
# 
# </details>
# </div>
# 
# 

# 
# ## Add extra variables and history files: **``fincl``**
# 
# You can output up to 10 history files: **``h0``**, **``h1``**, …, **``h9``**. 
# - The **``h0``** file contains the default variables or fields. (These are the variables you get by default without doing any modification to the namelist or code).
# 
# - For the files **``h1``** to **``h9``**, the user must specify the variables to output. 
# 
# To control the list of fields in the history files, use the namelist variable **``fincl``**
# - **``fincl1``** controls the fields in **``h0``** 
# - **``fincl2``** controls the fields in **``h1``** 
# - ...
# - **``fincl10``** controls the fields in **``h9``** 
# 
# For example, to add the field `PRECT` to the `h0` file, use the line:
# ```
#     fincl1 = 'PRECT' 
# ```
# 
# 
# <div class="alert alert-info">
# <strong>Evaluate your understanding</strong>
# 
# What is the namelist setting to add:
# - a hourly history `h1` with the variables U, V, T 
# - and a daily history `h2` with the variable PRECT 
# - and output 10 time samples in `h1` and `h2` ? 
# </div>
# 
# <div class="alert alert-success">  
# <details>  
# 
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
# 
# Add the following lines to `user_nl_cam`:
# ```    
#     nhtfrq = 0, -1, -24 
#     mfilt = 1, 10, 10 
#     fincl2 = 'U', 'V', 'T' 
#     fincl3 = 'PRECT'
# ```
# 
# </details>
# </div>
# 
# 

# 
# ## Averaging flag for the **``fincl``** variables 
# 
# Using a `:` following a field gives the averaging flag for the output field. 
# 
# Valid flags are: 
# - **``A``** ==> Average
# - **``B``** ==> GMT 00:00:00 average
# - **``I``** ==> Instantaneous
# - **``M``** ==> Minimum
# - **``X``** ==> Maximum
# - **``L``** ==> Local-time
# - **``S``** ==> Standard deviation
# 
# For instance, the line:
# ```
#      fincl1 = 'PRECT:M' 
# ```
# is used to add the minimum of ``PRECT`` to the file ``h0``
# 
# 
# <div class="alert alert-info">
# <strong>Evaluate your understanding</strong>
# 
# What happens if we set in `user_nl_cam`:
# ```  
#     fincl2   = 'T:I','Q:I','U:I','V:I'
#     nhtfrq   = 0, -3 
#     mfilt   = 1, 8
# ```
# 
# </div>
# 
# <div class="alert alert-success">  
# <details>  
# 
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
# 
# In addition to the monthly history file `h0`, 
# - we will also output the file `h1` with instantaneous values of <strong>T, Q, U, and V</strong>. 
# - These variables will be output every <strong>3 hours</strong>, resulting in <strong>8 time samples</strong> in each `h1` file. 
# - A new file will be created <strong>every day</strong>.
# 
# </details>
# </div>
# 
# 

# In[ ]:




