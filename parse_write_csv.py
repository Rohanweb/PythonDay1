import csv

with open("text.csv","r") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    with open("new_text.csv","w") as new_file:
        fieldnames=['Name','Salary']
        csv_writer=csv.DictWriter(new_file,fieldnames=fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            print(line)
            del line['Code']
            csv_writer.writerow(line)


