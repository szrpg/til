# -*- coding: utf-8 -*-
import folium


m = folium.Map(
    location=[35.681715, 139.767178],
    tiles='Stamen Toner',
    zoom_start=13
)

m.save('map.html')
