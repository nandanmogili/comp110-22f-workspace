from csv import DictReader

file_handle = open("data.weather/csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)

for row in csv_reader:
    print(row)

file_handle.close()