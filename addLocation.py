# -*- coding: utf-8 -*-

import simplejson as json

jsonfile_skolenavn = json.load(open('skolenavn.py-felles-2016-17.json'))
jsonfile_skoledata = json.load(open('./Data/skoler.json'))

temp = []
for skoler in jsonfile_skolenavn:
    skole = skoler['skole'].lower()

    for o in jsonfile_skoledata:
        if o['Skolenavn'].lower() == skole:
            skoler['skole'] = skoler['skole']
            skoler['Logitude'] = o['Longitude']
            skoler['Latitude'] = o['Latitude']
            skoler['Hjemmeside'] = o['Hjemmeside']
    temp.append(skoler)
print temp[2]['skole']
open("skoledata-felles-2016-17.json", 'w').write(
    json.dumps(temp, sort_keys=True, indent=4, separators=(',', ': '))
)
