import csv
# Reading data from csv using dictionary format
with open("text.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line)
# Reading data from csv using list format
with open("text.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)

#print(csv_reader)
