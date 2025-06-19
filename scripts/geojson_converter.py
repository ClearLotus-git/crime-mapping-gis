import pandas as pd
import geojson

df = pd.read_csv('data/crime_data_sample.csv')
features = []

for _, row in df.iterrows():
    point = geojson.Point((row['Longitude'], row['Latitude']))
    properties = {k: row[k] for k in df.columns if k not in ['Longitude', 'Latitude']}
    features.append(geojson.Feature(geometry=point, properties=properties))

feature_collection = geojson.FeatureCollection(features)

with open('geo/crimes.geojson', 'w') as f:
    geojson.dump(feature_collection, f)
