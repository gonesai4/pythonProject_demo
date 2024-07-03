import csv

"""
# writing the data to csv file
# static approach to reading the data using list format (data) with writer

fields = ["EmpId", "EmpName", "EmpAge", "EmpAddress"]
data = [[1, "Emp1", 25, "Hyd"], [2, "Emp2", 35, "Bngl"], [3, "Emp3", 30, "Mumbai"]]

with open('employee.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    writer.writerows(data)

"""

# dynamic approach to reading the data using dictionary format (data) with DictWriter

fields = ["EmpId", "EmpName", "EmpAge", "EmpAddress"]
data = [
            {
                "EmpId": 1,
                "EmpName": "Emp1",
                "EmpAge":25,
                "EmpAddress": "Hyd"
            },
            {
                "EmpId": 2,
                "EmpName": "Emp2",
                "EmpAge": 35,
                "EmpAddress": "Bngl"
            },
            {
                "EmpId": 3,
                "EmpName": "Emp3",
                "EmpAge": 30,
                "EmpAddress": "Mumbai"
            }
        ]
with open('employee_dict.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerows(data)


