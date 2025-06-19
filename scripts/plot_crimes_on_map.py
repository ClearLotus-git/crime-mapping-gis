import pandas as pd
import folium

df = pd.read_csv('data/crime_data_sample.csv')

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)
for _, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Crime Type']).add_to(m)

m.save('outputs/crime_map.html')
