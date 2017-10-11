import folium
import pandas

def elevation_color(elev):
    if elev<1500:
        return "green"
    elif elev>1500 and elev<3000:
        return "orange"
    else:
        return "red"

# create a map object (removed tiles="Mapbox Bright")
map=folium.Map(location=[38.76, -9.2], zoom_start=10)
# create a feature group
group=folium.FeatureGroup(name="my map")

# store data from a txt file in python
data=pandas.read_csv("Volcanoes_USA.txt")
# separate the latitudes and longitudes into individual pyhton lists
latitude=list(data["LAT"])
longitude=list(data["LON"])
elevation=list(data["ELEV"])

# iterate through a list of latitudes and longitudes to create multiple markers
# the zip object returns a tuple with two values from the lists and its next() method increments them at the same time
for lat,lon,elev in zip(latitude, longitude, elevation):
    # create a marker on the map and display the elevation of each marked spot
    group.add_child(folium.Marker(location=[lat,lon], popup="elevation: "+str(elev)+"m", icon=folium.Icon(color=elevation_color(elev))))

# add feature group properties to our map
map.add_child(group)

# write html file
map.save("map-test.html")
