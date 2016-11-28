# Parse_skoledata
Filtrering av data og parsing fra .CSV til .JSON

## 1. changeEncoding.py
Gjesdal kommune sin CSV-fil er har ANSI enkoding. Denne endres til UTF8. I tillegg fjernes mellomrom som ikke skal være i CSV filen.  
  * Lagres som: _skolerute-gjesdal-kommune.csv_

## 2. filterCSV.py  
Fjerner en 'lærerdag'-kolonnen i CSV-filen til Stavanger kommune. Alle dager med kommentaren 'Lørdag' og 'Søndag' samt de uten kommentar fjernes. Tilsvarende filtrering er gjort i CSV-filen til Gjesdal samt endring av datoformat fra d.m.Y til Y-m-d.  
  * Lagres som: _skolerute-felles-2016-17.csv_

## 3. schoolNames.py
Tar inn 'skolerute-felles-2016-17.csv'. Fjerner alt bortsett fra skolenavn.  
  * Lagres som _skolenavn-felles-2016-17.csv_

## 4. mkJson.py
Gjør om alle .CSV filer til .JSON.  
  * _skolerute-felles-2016-17.csv_ --> _skolerute-felles-2016-17.json_

## 5.

## 6. ##

1. First ordered list item
2. Another item  
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.
