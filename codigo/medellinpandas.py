import pandas as pd
import matplotlib.pyplot as plt
from shapely import wkt
import geopandas as gpd

#load data

edges = pd.read_csv('calles_de_medellin_con_acoso.csv',sep=';')
edges['geometry'] = edges['geometry'].apply(wkt.loads)
edges = gpd.GeoDataFrame(edges)

area = pd.read_csv('calles_de_medellin_con_acoso.csv',sep=';')
area['geometry'] = area['geometry'].apply(wkt.loads)
area = gpd.GeoDataFrame(area)

#Create plot
fig, ax = plt.subplots(figsize=(20,12))

# Plot the footprint
area.plot(ax=ax, facecolor='green')

# Plot street edges
edges.plot(ax=ax, linewidth=0.3, edgecolor='black')

plt.tight_layout()
plt.show()


