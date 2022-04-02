#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import contextily as cx
import rtree


# # Mapping the entire US Logistics Network 

# ## Intermodal Freight Locations near Major US Ports

# In[2]:


## Importing our DataFrames

gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_RailTOFCCOFC.geojson"

rail_to_all_df = gpd.read_file(gisfilepath)

rail_to_all_df = rail_to_all_df.to_crs(epsg=3857)

rail_to_all_df


# In[3]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/shipping/Major_Ports.geojson"
major_ports_df = gpd.read_file(gisfilepath)
major_ports_df = major_ports_df.to_crs(epsg=3857)

major_ports_df


# ### Mapping Rail/Truck/Shipping Facilities Near to Major Ports in the United States

# In[4]:


major_transit_nodes = rail_to_all_df.sjoin_nearest(major_ports_df)
major_transit_nodes.explore()


# ## Air Freight to Truck Facilities Near Major Ports

# In[5]:


gisfilepath = "/Users/jnapolitano/Projects/rail-mapping/intermodal/Intermodal_Freight_Facilities_Air-to-Truck.geojson"
air_freight_to_truck_df = gpd.read_file(gisfilepath)
air_freight_to_truck_df = air_freight_to_truck_df.to_crs(epsg=3857)

air_freight_to_truck_df


# ### Calculating Air Freight Hubs Near Major Ports

# In[6]:


major_air_freight = air_freight_to_truck_df.sjoin_nearest(major_ports_df)
major_air_freight


# ### Mapping Air Freight Hubs with Access to a Port

# In[7]:


major_air_freight.explore()


# In[ ]:




