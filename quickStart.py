import csv

file = open('test.csv')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
# rows = []
for row in csvreader:
    print(row)
    # rows.append(row)
# print(rows)
file.close()
