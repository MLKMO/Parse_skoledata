# -*- coding: utf-8 -*-
import csv
import datetime

rem = ['lørdag','søndag','', '1']
skoledag = 'ja'

skolerute_stavanger = 'Data/skolerute-2016-17.csv'
skolerute_gjesdal = 'Data/skolerute-gjesdal-kommune.csv'
skolerute_felles = 'skolerute-felles-2016-17.csv'
skolenavn = 'skolenavn.py-felles-2016-17.csv'


# Remove 'laererdag' column from skolerute_stavanger
with open(skolerute_stavanger, 'rb') as inp, \
    open('Data/temp.csv', 'wb') as outp:
    rdr = csv.reader(inp)
    wtr = csv.writer(outp)
    for r in rdr:
        if len(r) == 6:
            del r[3]
            wtr.writerow(r)
outp.close()
inp.close()

with open('Data/temp.csv', 'rb') as inp, \
        open(skolerute_gjesdal, 'rb') as inp2, \
        open(skolerute_felles, 'wb') as out:
    writer = csv.writer(out)

    # Iterate through skolerute Stavanger and remove days without comments and saturday/sunday
    for row in csv.reader(inp):
        if row and row[2].lower() != skoledag and row[4].lower() not in rem:
            writer.writerow(row)

    # Iterate through skolerute Gjesdal to change date format and remove days without comments and saturday/sunday
    for row in csv.reader(inp2):
        if len(row) == 5 and row[0] != 'Dato':
            row[0] = datetime.datetime.strptime(row[0], '%d.%m.%Y').strftime('%Y-%m-%d')

            if row[2].lower() != skoledag and row[4].lower() not in rem:
                writer.writerow(row)

inp.close()
inp2.close()
out.close()
