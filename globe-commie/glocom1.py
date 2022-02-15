#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-15 2022-02-15 1.1
# glocom1.py

# ~ тема: глобальный коммивояжёр, вер. 1

import folium

mapafile = "mapa.html"

places = (
    ([59.942071,30.2677354], 'спб, дом'),
    ([55.8524374,37.4351729], "москва, пт"),
    ([54.990842,60.0880393], "чебаркуль"),
    ([54.8893953,83.0902525], "новосибирск, экваторная"),
    ([42.2619168,-71.072476], "сша, бостон, маша"),
    ([43.8811826,-79.4533959], "канада, ричмонд-хилл"),
    # ~ ([], ""),
    # ~ ([], ""),
    # ~ ([], ""),
    # ~ ([], ""),
    # ~ ([], ""),
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
