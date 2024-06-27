# Iterations or Loops

"""
top_cities = ["hyd", "bngl", "chennai", "mumbai", "delhi"]

# print(top_cities[0])
# print(top_cities[1])
# print(top_cities[2])
# print(top_cities[3])
# print(top_cities[4])

# syntax of for loop
for city in top_cities:
    print(city)

greeting = "Hello! Welcome to RNS"

for char in greeting:
    print(char)

users = { "A": 20000, "B": 15000, "C": 30000}

#print(users["A"])

# for user in users:
#     print(user)
#
# for user in users:
#     print(users[user])

for user in users.keys():
    print("User Name - " + user)

for sal in users.values():
    print("Salary - " + str(sal))

users = [("A", 20000, 25), ("B", 15000, 20), ("C", 30000, 30)]
print(len(users))

# for user in users:
#     #print(type(user))
#     print(user)
#     for detail in user:
#         print(detail)

# for user in users:
    #print(type(user))
    # print(user)
    # print("User Name is - " + user[0])
    # print("User Salary is - " + str(user[1]))
    # print("User Age is - " + str(user[2]))

for (name, sal, age) in users:
    print("User Name is - " + name)
    print("User Salary is - " + str(sal))
    print("User Age is - " + str(age))

"""

"""
# while loop

# while condition:
#     // while loop stmts

data = 1
while data <= 10:
    print(data)
    data = data + 1

"""

"""
# continue and break stmts

data = [1, 2, 0, 10, 15, 0, 35, 7, 0]

for item in data:
    if item == 0:
        continue
    else:
        print(item)

"""

data = [1, 2, 0, 10, 15, 0, 35, 7, 0]

item_found = False
search = 15
for item in data:
    if search == item:
        print("Hurray!!! found it")
        item_found = True
        break

if not(item_found):
    print("Sorry!!! Item not found")


