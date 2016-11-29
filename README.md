# Parse_skoledata
Filtrering av data og parsing fra .CSV til .JSON.  
Alle datasett er lastet ned fra Stavanger kommune sine nettsider:  
  * [Skolerute Stavanger](https://open.stavanger.kommune.no/dataset/skolerute-stavanger)  
  * [Skolerute Gjesdal](https://open.stavanger.kommune.no/dataset/skoleruten-for-gjesdal-kommune)
  * [Skoler Stavanger](https://open.stavanger.kommune.no/dataset/skoler-stavanger)
  
## 1. changeEncoding.py
Gjesdal kommune sin CSV-fil har ANSI enkoding. Denne endres til UTF8. I tillegg fjernes mellomrom som ikke skal være i CSV filen.  
  * Lagres som: _skolerute-gjesdal-kommune.csv_

## 2. filterCSV.py  
Fjerner en 'lærerdag'-kolonnen i CSV-filen til Stavanger kommune. Alle dager med kommentaren 'Lørdag' og 'Søndag' samt de uten kommentar fjernes. Tilsvarende filtrering er gjort i CSV-filen til Gjesdal samt endring av datoformat fra DD.MM.YYYY til YYYY-MM-DD.  
  * Lagres som: _skolerute-felles-2016-17.csv_

## 3. schoolNames.py
Tar inn 'skolerute-felles-2016-17.csv'. Fjerner alt bortsett fra skolenavn.  
  * Lagres som _skolenavn-felles-2016-17.csv_

## 4. mkJson.py
Gjør om alle .CSV filer til .JSON.  
  * _skolerute-felles-2016-17.csv_ --> _skolerute-felles-2016-17.json_
  * _skolenavn-felles-2016-17.csv_ --> _skolenavn-felles-2016-17.json_
  * _skoler.csv_ --> _skoler.json_

## 5. addLocation.py  
Henter informasjon om skolenes lokasjon og nettside fra _skoler.json_ og legger ilag med _skolenavn-felles-2016-17.json_. Skolene fra Gjesdal kommune har ikke utvidet informasjon om skolene sine. Disse er lagt inn manuelt i ettertid.
  * Lagres som: _skoledata-felles-2016-17.json_

## 6. generateDates.py
Genererer alle datoer fra 1. august til 31. juli på formatet YYYY-MM-DD som en .CSV-fil. Blir deretter parset til .JSON.
  * Lagres som: _datoer.json_

