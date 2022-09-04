import sys

from kivy.base import runTouchApp

from kivy_garden.mapview import MapMarker, MapView
from kivy_garden.mapview.clustered_marker_layer import ClusteredMarkerLayer
from kivy_garden.mapview.geojson import GeoJsonMapLayer
from kivy_garden.mapview.utils import get_zoom_for_radius, haversine

source = sys.argv[1]

options = {}
layer = GeoJsonMapLayer(source=source)

# try to auto center the map on the source
lon, lat = layer.center
options["lon"] = lon
options["lat"] = lat
min_lon, max_lon, min_lat, max_lat = layer.bounds
radius = haversine(min_lon, min_lat, max_lon, max_lat)
zoom = get_zoom_for_radius(radius, lat)
options["zoom"] = zoom

view = MapView(**options)
view.add_layer(layer)

marker_layer = ClusteredMarkerLayer(cluster_radius=200)
view.add_layer(marker_layer)

# create marker if they exists
count = 0


def create_marker(feature):
    global count
    geometry = feature["geometry"]
    if geometry["type"] != "Point":
        return
    lon, lat = geometry["coordinates"]
    marker_layer.add_marker(lon, lat)
    count += 1


layer.traverse_feature(create_marker)
if count:
    print("Loaded {} markers".format(count))

runTouchApp(view)
