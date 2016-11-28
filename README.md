# Parse_skoledata

1. ## changeEncoding.py
Gjesdal kommune sin CSV-fil er har ANSI enkoding. Denne endres til UTF8. I tillegg fjernes mellomrom som ikke skal være i CSV filen.
Lagres som: 'skolerute-gjesdal-kommune.csv'

2. ## filterCSV.py
Fjerner en 'lærerdag'-kolonnen i CSV-filen til Stavanger kommune. Alle dager med kommentaren 'Lørdag' og 'Søndag' samt de uten kommentar fjernes. Tilsvarende filtrering er gjort i CSV-filen til Gjesdal samt endring av datoformat fra d.m.Y til Y-m-d. Alt blir lagret i en fil: 'skolerute-felles-2016-17.csv'.

3. ## schoolNames.py
Tar inn 'skolerute-felles-2016-17.csv'. Fjerner alt bortsett fra skolenavn. Lagres som 'skolenavn-felles-2016-17.csv'.

4. ## mkJson.py

4. ##

5. ##

6. ##
