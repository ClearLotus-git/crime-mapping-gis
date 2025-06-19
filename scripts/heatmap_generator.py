import folium
from folium.plugins import HeatMap
import pandas as pd

df = pd.read_csv('data/crime_data_sample.csv')
heat_data = df[['Latitude', 'Longitude']].dropna().values.tolist()

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)
HeatMap(heat_data).add_to(m)

m.save('outputs/heatmap_example.html')
