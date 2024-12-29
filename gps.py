import folium
m = folium.Map(location=[37.7433, -122.4194], zoom_start=13)

folium.CircleMarker(
    location=[37.7433, -122.4194],
    radius=50,
    popup="san francisco",
    color="blue",
    fill=True,
    fill_color="blue"
).add_to(m)

# the map can only be displayed in jupyter notebook
m