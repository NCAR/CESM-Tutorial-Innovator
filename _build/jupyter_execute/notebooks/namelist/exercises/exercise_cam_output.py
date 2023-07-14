#!/usr/bin/env python
# coding: utf-8

# # Modify CAM output

# 
# <div class="alert alert-info">
# <strong>Exercise: Customize your CAM history files</strong><br><br>
#  
# Create a case called `b1850_high_freq` using the compset  ``B1850``  at ``f19_g17`` resolution. 
#     
# In addition to the monthly history file ``h0``, output:
# - ``h1`` file with **_instantaneous_** values of T, Q, U and V every **_24 hour_**.
# - ``h2`` file with **_time-average_** values of T, Q, U and V every **_3 hour_**.
# 
# Set your namelist so that you output:  
# - a **_single_** ``h1`` file with all the daily output for the month. 
# - **_multiple_** ``h2`` files, one for every day of the month.
# 
# Your goal is to produce:
# - one ``h1`` file with 31 timesteps and 
# - thirty-one ``h2`` files with 8 timesteps each.
# 
# Set the run length to **_1 month_** and make a 1-month run.
# 
# </div>
# 

# 
# <div class="alert alert-warning">  
# <details>
# 
# <summary> <font face="Times New Roman" color='blue'>Click here for hints</font> </summary>
#     
# **# How do I compile?**
# 
# You can compile with the command:
# ```
# qcmd -- ./case.build
# ```
# 
# **# How do I control the output?**
# 
# Use namelist variables: ``nhtfrq``, ``mfilt``, ``fincl``. 
# 
# Look at the online documentation for these variables.
# 
# **# How do I check my solution?**
# 
# When your run is completed, go to the archive directory and navigate to the subdirectory `atm/hist`
# 
# ```
# cd /glade/scratch/$USER/archive/b1850_high_freq
# cd atm/hist
# ```
# 
# (1) Check that your archive directory contains the files:
# 
# - ``h0`` files
# ```
# b1850_high_freq.cam.h0.0001-01.nc
# ```
# - ``h1`` files
# ```
# b1850_high_freq.cam.h1.0001-01-01-00000.nc
# b1850_high_freq.cam.h1.0001-02-01-00000.nc
# ```
# - ``h2`` files
# ```
# b1850_high_freq.cam.h2.0001-01-01-00000.nc
# …
# b1850_high_freq.cam.h2.0001-01-31-00000.nc
# b1850_high_freq.cam.h2.0001-02-01-00000.nc
# ```
# 
# (2) Compare the contents of the ``h1`` and ``h2`` files using ``ncdump``.
# 
# ```
# ncdump -h b1850_high_freq.cam.h1.0001-01-01-00000.nc
# ncdump -h b1850_high_freq.cam.h2.0001-01-01-00000.nc
# ```
# 
# (3) Check the number of timesteps in the ``h1`` and the ``h2`` files.
# Look at the sizes of the files. 
# 
# </details>
# </div>
# 

# 
# <div class="alert alert-success">   
# <details>
# <summary><font face="Times New Roman" color='blue'>Click here for the solution</font></summary><br>
#                 
# **# Create a new case**
# 
# Create a new case `b1850_high_freq` with the command:
# ```
# cd /glade/work/$USER/code/my_cesm_code/cime/scripts/
# ./create_newcase --case ~/cases/b1850_high_freq  --compset B1850 --res f19_g17 
# ```
# 
# **# Setup**
#     
# Invoke case.setup with the command:
#     
# ```    
# cd ~/cases/b1850_high_freq 
# ./case.setup
# ```
# 
# **# Customize namelists**
#     
# Edit the file `user_nl_cam` and add the lines:
# ```
#  nhtfrq = 0, -24, -3
#  mfilt = 1, 31, 8 
#  fincl2 = 'T:I','Q:I','U:I','V:I'
#  fincl3 = 'T','Q','U','V'
# ```
#  
# **# Set run length**
#     
# Change the `run length`:
# ```   
# ./xmlchange STOP_N=1,STOP_OPTION=nmonths
# ```
# 
# **# Change the job queue and account number**
# 
# If needed, change `job queue` and `account number`. <br>
# For instance, to run in the queue `regular` and the project number `P93300642`, use the command:
# ```  
# ./xmlchange JOB_QUEUE=regular,PROJECT=P93300642
# ```
# 
# **# Build and submit**
#     
# Build the model and submit your job:
# ```
# qcmd -- ./case.build
# ./case.submit
# ```
# 
# ____
#     
# **# Look at your solution**
# 
# When the run is completed, look into the archive directory for: 
# `b1850_high_freq`.  
#     
# (1) Check that your archive directory on cheyenne (The path will be different on otehr machines): 
# ```
# cd /glade/scratch/$user/archive/b1850_high_freq/atm/hist
# ls 
# ```
# 
# (2) Compare the contents of the ``h1`` and ``h2`` files using ``ncdump``.
# Look at the variables attributes. What is the difference between the 2 files ? 
# 
# The file with the instantaneous output ``h1`` have no cell_methods attribute while the average output ``h2`` has a attribute: 
# ```
# cell_methods = "time: mean"
# ```
# 
# For instance for the field Q.
# 
# In the instantaneous file ``b1850_high_freq.cam.h1.0001-01-01-00000.nc``
# ```
# float Q(time, lev, lat, lon) ;
#                 Q:mdims = 1 ;
#                 Q:units = "kg/kg" ;
#                 Q:mixing_ratio = "wet" ;
#                 Q:long_name = "Specific humidity" ;
# ```
# In the time-averaged file  ``b1850_high_freq.cam.h2.0001-01-01-00000.nc``
# ```
# float Q(time, lev, lat, lon) ;
#                 Q:mdims = 1 ;
#                 Q:units = "kg/kg" ;
#                 Q:mixing_ratio = "wet" ;
#                 Q:long_name = "Specific humidity" ;
#                 Q:cell_methods = "time: mean" ;
# ```
# (3) Check the number of timesteps in the h1 and the h2 files. 
# 
# - ``h1`` contains 31 time samples.  
# In the netcdf file,  
# ```
# time = UNLIMITED ; // (31 currently)
# ```
# - ``h2`` contains 8 time samples 
# In the netcdf file, 
# ```
# time = UNLIMITED ; // (8 currently)
# ```
# - Check the size of the files
# ```
# du –ks –h /glade/scratch/$user/archive/b1850_high_freq/atm/hist/*
# ```
# ```
# 234M    b1850_high_freq.cam.h0.0001-01.nc
# 
# 210M    b1850_high_freq.cam.h1.0001-01-01-00000.nc
# 7.0M    b1850_high_freq.cam.h1.0001-02-01-00000.nc
# 
# 55M     b1850_high_freq.cam.h2.0001-01-01-00000.nc
# 55M     b1850_high_freq.cam.h2.0001-01-02-00000.nc
# ...
# 55M     b1850_high_freq.cam.h2.0001-01-31-00000.nc
# 7.0M    b1850_high_freq.cam.h2.0001-02-01-00000.nc
# ```
# 
# </details>
# </div>
# 
# 

# In[ ]:




