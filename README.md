# Parse_skoledata
Filtrering av data og parsing fra .CSV til .JSON

## 1. changeEncoding.py
Gjesdal kommune sin CSV-fil er har ANSI enkoding. Denne endres til UTF8. I tillegg fjernes mellomrom som ikke skal være i CSV filen.
  *Lagres som: 'skolerute-gjesdal-kommune.csv'

## 2. filterCSV.py
Fjerner en 'lærerdag'-kolonnen i CSV-filen til Stavanger kommune. Alle dager med kommentaren 'Lørdag' og 'Søndag' samt de uten kommentar fjernes. Tilsvarende filtrering er gjort i CSV-filen til Gjesdal samt endring av datoformat fra d.m.Y til Y-m-d. 
  *Lagres som: 'skolerute-felles-2016-17.csv'.

## 3. schoolNames.py
Tar inn 'skolerute-felles-2016-17.csv'. Fjerner alt bortsett fra skolenavn. 
  *Lagres som 'skolenavn-felles-2016-17.csv'.

## 4. mkJson.py
Gjør om alle .CSV filer til .JSON. 
 *'skolerute-felles-2016-17.csv' --> 'skolerute-felles-2016-17.json'

## 4.

## 5. ##

## 6. ##
