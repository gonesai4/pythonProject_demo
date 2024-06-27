# set data type

"""
Defining list:  []    mutable
Defining tuple: ()    immutale
Defining set: {}      not following sequence order, it doesn't accept duplicate data


data = {10, 10.5, True, "RNS", "Tech"}
print(type(data))
print(data)

# duplicate data adding
data = {10, 10.5, True, "RNS", "Tech"}
print(len(data))
print(data)
data = {10, 10.5, True, "RNS", "Tech", 10, "Tech"}
print(len(data))
print(data)
data = [10, 10.5, True, "RNS", "Tech", 10, "Tech"]
print(len(data))
print(data)

# inserting element
data = {10, 10.5, True, "RNS", "Tech"}
data[3] = 1000 # error stmt
print(data)

# adding and removing element
data = {10, 10.5, True, "RNS", "Tech"}
data.add(1000)
data.remove(True)
print(data)

# reading and printing from set
data = {10, 10.5, True, "RNS", "Tech"}
for item in data:
    print(item)

"""
# removing duplicates from list
my_list = [1, 3, 5, 1, 9, 5, 1]
my_set = list(set(my_list))
print(my_set)




