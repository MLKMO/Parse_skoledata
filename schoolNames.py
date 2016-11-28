# -*- coding: utf-8 -*-
import csv

skolerute_felles = 'skolerute-felles-2016-17.csv'
skolenavn = 'skolenavn-felles-2016-17.csv'


# Create CSV-file with school names only.
with open(skolerute_felles, 'rb') as inp, \
        open(skolenavn, 'wb') as out:
    writer = csv.writer(out)
    reader = csv.reader(inp)

    pre_line = next(reader)[1]
    print pre_line
    writer.writerow([pre_line])

    for row in reader:
        cur_line = row[1]
        if pre_line != cur_line:
            writer.writerow([cur_line])
        pre_line = cur_line


inp.close()
out.close()
