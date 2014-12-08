#!/usr/bin/python

import json
import sys

# Citeste datele din fisierul de intrare
json_data = open('room_info.json')

# Converteste continutul
try:
    data = json.load(json_data)
except ValueError as ex:
    print "ERROR: fisier JSON incorect formatat"
    sys.exit(1)

# Afiseaza tabelul
for room in data:
    print "Sala: %s (%s locuri)" % (room["nume"], room["locuri"])
    print "Este ocupata:"
    for day in room["ocupat"]:
        print "  " + day + ": " + ', '.join(room["ocupat"][day])
    print "\n"
