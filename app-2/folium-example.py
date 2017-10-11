import folium

# create a map object (removed tiles="Mapbox Bright")
map = folium.Map(location=[38.76, -9.2], zoom_start=10)
# create a feature group
group=folium.FeatureGroup(name="my map")
# create a marker on the map
group.add_child(folium.Marker(location=[38.76, -9.2], popup="gucci gang gucci gang", icon=folium.Icon(color="green")))
map.add_child(group)

map.save("map-test.html")
