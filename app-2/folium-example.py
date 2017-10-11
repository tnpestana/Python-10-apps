import folium

# create a map object (removed tiles="Mapbox Bright")
map = folium.Map(location=[38.76, -9.2], zoom_start=10)
# create a feature group
group=folium.FeatureGroup(name="my map")
# iterate through a list of locations (wich are also lists of coordinates) to create multiple markers
for coordinates in [[38.76, -9.2], [38.75, -9.21]]:
    # create a marker on the map
    group.add_child(folium.Marker(location=coordinates, popup="gucci gang gucci gang", icon=folium.Icon(color="green")))

map.add_child(group)

map.save("map-test.html")
