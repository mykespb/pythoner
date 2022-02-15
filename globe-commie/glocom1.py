#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-15 2022-02-15 3.1
# glocom1.py

# ~ тема: глобальный коммивояжёр

import folium
from geopy.distance import great_circle

mapafile = "mapa.html"

places = (
    ([59.942071,30.2677354], 'спб, дом', "MK"),
    ([55.8524374,37.4351729], "москва, пт", "PT"),
    ([54.990842,60.0880393], "чебаркуль", "CH"),
    ([54.8893953,83.0902525], "новосибирск, экваторная", "NE"),
    ([42.2619168,-71.072476], "сша, бостон, маша", "BM"),
    ([43.8811826,-79.4533959], "канада, ричмонд-хилл", "RH"),
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
        loko, desc, code = place
        folium.Marker(loko, popup=desc, tooltip=code).add_to(mapa)

    # ~ mapa.save(mapafile)

do1()

# ok
def dists():
    """рассчитать расстояния"""
    for p1 in places:
        for p2 in places:
            if p1 == p2:
                dist = 0
            else:
                ll1 = p1[0]
                ll2 = p2[0]
                dist = great_circle(ll1, ll2).km
            print("%10.3f" % dist, end=" ")
        print()

dists()

     # ~ 0.000    620.777   1848.135   3124.727   6603.888   6831.496 
   # ~ 620.777      0.000   1426.339   2834.176   7212.999   7450.423 
  # ~ 1848.135   1426.339      0.000   1462.649   8256.612   8377.258 
  # ~ 3124.727   2834.176   1462.649      0.000   8938.325   8909.044 
  # ~ 6603.888   7212.999   8256.612   8938.325      0.000    703.822 
  # ~ 6831.496   7450.423   8377.258   8909.044    703.822      0.000 

# ~ ok
def liner1():
    """отрисовать 1 линию"""
    p1, p2 = places[:2]
    ll1 = p1[0]
    ll2 = p2[0]
    folium.PolyLine([ll1, ll2], color="red").add_to(mapa)

# ~ liner1()

def liner2():
    """рассчитать расстояния"""
    for p1 in places:
        for p2 in places:
            if p1 != p2:
                ll1 = p1[0]
                ll2 = p2[0]
                folium.PolyLine([ll1, ll2], color="red").add_to(mapa)

liner2()

mapa.save(mapafile)
