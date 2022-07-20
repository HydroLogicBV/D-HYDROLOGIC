#!/usr/bin/env python
# coding: utf-8

# # Usage
# D-Hydro results stored in history files (_his.nc) can be extracted and processed using the provided his(tory file)reader.
# By default *hisreader<span>.py</span>* extracts timeseries for all observation points and structures for which output is provided and stores them as individual pandas-compatible csv files.
# Advanced usage allows the direct processing of the results, e.g. to combine simulated results with measurements and to generate plots for quick inspection of the results.

# ## Import hisreader
# Add hisreader to path and import HisResults

# In[1]:


import sys  
sys.path.insert(0, 'D:\Work\git\D-HYDROLOGIC\src')
from hisreader import HisResults


# ## Load results
# Load example model reults and make a quick plot to inspect the data for a measurement station (WS000369 in this case).

# In[2]:


input_path = r"D:\Work\git\D-HYDROLOGIC\data\\"
Results = HisResults(inputdir=input_path, outputdir=input_path + r"\csv\\")

Results.WS000369.simulated_plot("waterlevel")


# It is also possible to load station names programatically, usefull if you for example want plots for all observation stations.

# In[3]:


obj_name = Results.structure_list[0][0]
print(obj_name)
getattr(Results, obj_name).simulated_plot("waterlevel")


# ## Save results as csv files
# providing an *output_path* is optional, otherwise it will use the path provided before

# In[4]:


Results.write_csv(output_path = input_path + r"\csv\\")


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
