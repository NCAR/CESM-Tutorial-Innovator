#!/usr/bin/env python
# coding: utf-8

# # Overview 
# 
# There are a number of ways that the model can be modified via namelist settings. These values control the way the code is run. 
# 
# The **namelist variables** include settings to control over output, tune the model for various quantities, and many other options. For instance, the output frequency in the different components can be controlled via the namelists. 
# 
# <div class="alert alert-info" style="text-align: left;">
# 
# The **steps** to modify the **namelists** are:
# 
# In ``$CASEROOT`` 
# - edit the ``user_nl_xxx`` files.
# - generate the namelists by running ``./preview_namelists``. 
#   
#   
# This results in the creation of component namelists, the ``*_in`` files (i.e. `atm_in`, `lnd_in`, and so on). 
# 
# The ``*_in`` files are located  in ``$CASEROOT/CaseDocs/`` and in ``$RUNDIR``.
#   
# </div>
# 
# 
# An overview of the CESM directories and the location of the namelist files is showed in *Figure 1*
# 

# ___
# ![CESM directories and namelists](../../images/namelist/CESM_directories_and_namelists.png)
# <p style="text-align: center;"> Figure 1: Overview of the CESM directories and the namelist files. </p>
# 
# ___

# 
# The ``*_in`` files **should not be directly edited**. Any manual changes of the ``*_in`` files will be overwritten when you compile or submit the run. 
# 
# Note that step ``./preview_namelists`` is **optional** as the script *preview_namelists* is also called when you build the model. 
# 
# Note that you cannot change the namelist variables: 
# - after the run is submitted 
# - or when `CONTINUE_RUN=TRUE`. 
# 

# <div class="alert alert-info">
# 
# Complete documentation about the namelist variables can be found on the [CESM webpage.](https://www2.cesm.ucar.edu/models/cesm2/settings/current/)
# 
# </div>

# In[ ]:




