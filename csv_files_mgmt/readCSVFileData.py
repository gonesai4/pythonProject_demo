import csv

"""
# reading the data from csv file
# static approach to reading the data using csv.reader
with open('empdata.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))
    for row in reader:
        # print(row)
        print(f'{row[1]} is located in {row[2]}')

# dynamic approach to reading the data using csv.DictReader

with open('empdata.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print(type(reader))
    for row in reader:
        # print(row)
        print(f"{row['EmpName']} is located in {row['EmpAddress']}")


"""





