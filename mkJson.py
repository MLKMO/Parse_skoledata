import csv
import json

csvfile = open('skolerute-felles-2016-17.csv', 'rU')
csvfile_skolenavn = open('skolenavn.py-felles-2016-17.csv', 'rU')
csvfile_skoledata = open('./Data/skoler.csv', 'rU')

jsonfile = open('skolerute-felles-2016-17.json', 'w')
jsonfile_skolenavn = open('skolenavn.py-felles-2016-17.json', 'w')
jsonrile_skoledata = open('./Data/skoler.json', 'w')

# Open the CSV
reader = csv.DictReader(csvfile)
reader_skolenavn = csv.DictReader(csvfile_skolenavn)
reader_skoledata = csv.DictReader(csvfile_skoledata)

# Parse the CSV into JSON
out = json.dumps([row for row in reader], ensure_ascii=False, encoding="utf-8", sort_keys=True,
                 indent=4, separators=(',', ': '))
out2 = json.dumps([row for row in reader_skolenavn], ensure_ascii=False, encoding="utf-8", indent=4)
out3 = json.dumps([row for row in reader_skoledata], ensure_ascii=False, encoding="utf-8", sort_keys=True,
                 indent=4, separators=(',', ': '))
print "JSON parsed!"

# Save the JSON
jsonfile.write(out)
jsonfile_skolenavn.write(out2)
jsonrile_skoledata.write(out3)
print "JSON saved!"


csvfile.close()
jsonfile.close()