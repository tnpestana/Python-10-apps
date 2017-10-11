import folium
import pandas

# create a map object (removed tiles="Mapbox Bright")
map=folium.Map(location=[38.76, -9.2], zoom_start=10)
# create a feature group
group=folium.FeatureGroup(name="my map")

# store data from a txt file in python
data=pandas.read_csv("Volcanoes_USA.txt")
# separate the latitudes and longitudes into individual pyhton lists
latitude=list(data["LAT"])
longitude=list(data["LON"])

# iterate through a list of latitudes and longitudes to create multiple markers
# the zip object returns a tuple with two values from the lists and its next() method increments them at the same time
for lat, lon in zip(latitude, longitude):
    # create a marker on the map
    group.add_child(folium.Marker(location=[lat,lon], popup="gucci gang gucci gang", icon=folium.Icon(color="green")))

# add feature group properties to our map
map.add_child(group)

# write html file
map.save("map-test.html")
