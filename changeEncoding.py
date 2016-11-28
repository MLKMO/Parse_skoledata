# -*- coding: utf-8 -*-
import csv
import string
import io
import shutil

file_path_ansi = './Data/skolerute-gjesdal.csv'
file_path_utf8 = './Data/tempGjestdal.csv'
file_path_utf8_stripped = './Data/skolerute-gjesdal-kommune.csv'

# Change encoding from ANSI to utf8
with io.open(file_path_ansi, encoding='latin-1', errors='ignore') as source:
    with io.open(file_path_utf8, mode='w', encoding='utf-8') as target:
        shutil.copyfileobj(source, target)

# Remove blank spaces from csv-file
with open(file_path_utf8) as infile:
    reader = csv.reader(infile, delimiter=",")
    with open(file_path_utf8_stripped, "wb") as outfile:
        writer = csv.writer(outfile)
        for rec in reader:
            writer.writerow(map(string.strip, rec))

infile.close()
outfile.close()
