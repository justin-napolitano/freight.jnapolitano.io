#!/usr/bin/env python
# coding: utf-8

# # Mapping US and Texas Rail Lines
# 
# ## About
# 
# Mapping Rail Lines and Rail Nodes in the United States.  
# 
# This is a precursor project to one that will create a graph of rail, shipping, trucking, and air freight transport networks for analysis.

# ## Import Functions

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx


# ## Reading Node Shape Data into gpd DF

# In[2]:


shapefilepath = "/Users/jnapolitano/Projects/rail-mapping/North_American_Rail_Nodes/North_American_Rail_Nodes.shp"

node_df = gpd.read_file(shapefilepath)



node_df.head()


# ## Checking Cooridindate System.  
# 
# The coordinate system must be in the epsg 3857 format to overlay.

# In[3]:


node_df.crs


# ### Converting to EPSG 3857 System

# In[4]:


df_wm = node_df.to_crs(epsg=3857)


# ## Plotting Every Rail node in the United States, Mexico, and Canada

# In[5]:


ax = df_wm.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
cx.add_basemap(ax, zoom=5)


# ## Discussion of results Thus Far
# 
# ### Detail
# 
# Mapping every node in the data set produces too much noise to be useful.  It is interesting though that the rail coverage in north america nearly covers the entire continent.
# 
# ### Next Steps
# 
# I will decrease the marker size to see if it improved the detail and usability of the plot.

# ## Plotting Data with Smaller Markers

# In[6]:


ax = df_wm.plot(figsize=(10, 10), alpha=0.5, edgecolor='k', markersize = .5)
cx.add_basemap(ax, zoom=7)


# ### Results
# We have increased our detail to an acceptable level to understand just how interconnected the rail system is in North America.  The data plotted thus far is a collection of all points. Next, we'll review the data to identify points that may yield more interesting results

# ## Filtering the Dataset

# ### Printing the head of the dataframe for review

# In[7]:


df_wm.head()


# #### Understanding the Fields
# 
# The data source does not detail the fields very well.  https://geo.dot.gov/mapping/rest/services/NTAD/North_American_Rail_Nodes/MapServer/0
# 
# Unfortunately, we'll have to infer their meaning.

# ##### Unique PASSNGR Values
# 
# My best guess is that these values designate nodes that serve passenger transport.

# In[8]:


df_wm['PASSNGR'].unique()


# ##### Results
# 
# It is still not clear what these values translate to.  I'll have to continue investigating.

# ##### Unique PASSNGRSTN Values
# 
# My best guess is that these values designate nodes that serve as passenger transport terminals.

# In[9]:


results = df_wm['PASSNGRSTN'].unique()
print(results)


# ###### Results
# 
# I think my guess is correct.  These are definetely commmuter stations.  I recognize Boston Landing and 59th ST. (U. of Chicago) from travel.  I can't assume however that these are only passenger stations.  They may also be freight connections.  Therefore, I cannot yet eliminate them from the dataset.

# ##### Unique FRADISTRICT
# 
# These values are associated with Federal Railroad Association Districts.  I was able to find the the key for the values at https://railroads.dot.gov/divisions/regional-offices/safety-management-teams. 
# 
# This will be useful to investigate the bottle necks by railway and safety zone, but still does not help me to completely eliminate commuter and passengers.

# In[10]:


results = df_wm['FRADISTRCT'].unique()
print(results)


# ## Attempting to Discern meaning from an Accompanying Dataset
# 
# I could not infer exactly what the node data means without the keys.  I will have to look online for more information.  In the mean time however I will map and explore the rail line data.

# ### Loading the Rail Line Data

# In[11]:


shapefilepath = "/Users/jnapolitano/Projects/rail-mapping/North_American_Rail_Lines/North_American_Rail_Lines.shp"

line_df = gpd.read_file(shapefilepath)



line_df.head()


# ## Checking Cooridindate System.  
# 
# The coordinate system must be in the epsg 3857 format to overlay.

# In[12]:


line_df.crs


# ### Converting to EPSG 3857 System

# In[13]:


line_wm = line_df.to_crs(epsg=3857)


# ## Plotting Every Rail Line in the United States, Mexico, and Canada

# In[14]:


ax = line_wm.plot(figsize=(10, 10), alpha=0.5, edgecolor='k', markersize = .5)
cx.add_basemap(ax, zoom=7)


# #### Printing Data Fields

# In[15]:


line_wm.columns


# #### Creating a Map of Texas Rail Lines
# 
# Texas is an important freight destination.  The state possess many natural important ports and freight stations.

# ##### Filtering the data set for Texas state Lines.
# 
# FIPS codes can be found at https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696
# 
# Texas is recognized as code 48.

# In[16]:


#Getting Unique values to identify 48 is in the set 
print(line_wm['STFIPS'].unique())
#48 is a strin in the dataset do not compare it to an integer!!
texas_lines_df = line_wm.loc[line_wm['STFIPS'] == '48']
#print(texas_lines_df)
#print(texas_lines_df)


# ##### Mapping Texas Non-Interactive

# In[17]:


ax = texas_lines_df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k', markersize = .5)
cx.add_basemap(ax, zoom=6)


# In[ ]:





# ##### Mapping an Interactive Map

# In[18]:


texas_lines_df.explore()

