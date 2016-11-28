import datetime
import json
import csv

date1 = '2016-08-01'
date2 = '2017-07-31'
start = datetime.datetime.strptime(date1, '%Y-%m-%d')
end = datetime.datetime.strptime(date2, '%Y-%m-%d')
step = datetime.timedelta(days=1)
dates = ["dato"]

while start <= end:
    dates.append(str(start.date()))
    start += step

with open('temp.csv', 'w') as csvFile:
    wrt = csv.writer(csvFile)
    for row in dates:
        wrt.writerow([row])

csvFile.close()

with open('temp.csv', 'r') as inp, \
    open('datoer.json', 'w') as outp:
    reader = csv.DictReader(inp)
    out = json.dumps([row for row in reader], ensure_ascii=False, encoding="utf-8", sort_keys=True,
                     indent=4, separators=(',', ': '))
    outp.write(out)

inp.close()
outp.close()

