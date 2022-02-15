#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-15 2022-02-15 1.0
# glocom1.py

# ~ тема: глобальный коммивояжёр, вер. 1

import folium

mapafile = "mapa.html"

places = (
    ([59.942071,30.2677354], 'дом спб'),
)

mapa = folium.Map(location=places[0][0], zoom_start=8)

# ok
def do1():
    """просто делаем карту и показываем дом"""
    for place in places:
        loko, tooltip = place
        folium.Marker(loko, popup=tooltip, tooltip=tooltip).add_to(mapa)

    mapa.save(mapafile)

do1()
