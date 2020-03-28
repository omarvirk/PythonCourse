import folium
import pandas

def marker_color(volcano_height):
    if volcano_height < 1000:
        return 'green'
    elif 1000 <= volcano_height < 2000:
        return 'yellow'
    else:
        return 'red'

volcano_data = pandas.read_csv("Volcanoes.txt")
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
name = list(volcano_data["NAME"])
hheight = list(volcano_data["ELEV"])

map = folium.Map(location = [lat[0],lon[0]], zoom_start = 6, tiles="Stamen Terrain")
features = folium.FeatureGroup("Mapq_feat")

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

for lt,ln,nm, h in zip(lat,lon,name,hheight): 
    iframe = folium.IFrame(html= html %("Volcano "+nm,nm,h), width= 100, height = 200, ratio=60)
    #features.add_child(folium.Marker(location = [lt,ln], popup= folium.Popup(iframe), icon= folium.Icon(color=marker_color(h))))
    features.add_child(folium.CircleMarker(location= [lt,ln], radius= 5,popup= folium.Popup(iframe), tooltip= 'Volcano', 
    fill_color = marker_color(h), color = 'grey', fill_opacity= 0.7 ))

features.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: 
{'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(features)
map.save("Map1.html")