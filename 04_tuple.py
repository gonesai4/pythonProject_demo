# Tuple Collection of data types

"""
List is Mutable:
-insert the data, append, delete

String and Tuple: are immutable
-append the data at the last element


# declaring tuple with paranthesis
tuple_data = (1, 20, "RNS")
print(type(tuple_data))
print(tuple_data[2])

# inserting the element in tuple
tuple_data = (1, 20, "RNS")
#tuple_data[1] = 50   # error stmt
print(len(tuple_data))

#deleting element from tuple
tuple_data = (1, 20, "RNS")
# del tuple_data[2]  # error stmt
print(tuple_data)

# we can use without paranthesis also
# defining the data with ","
one_element_tuple = 500,
print(type(one_element_tuple))
print(one_element_tuple)

two_element_tuple = 500, "RNS"
print(type(two_element_tuple))
print(two_element_tuple)

# reading items using slicing
tuple_data = (1, 20, "RNS", "Tech", "12 years")
print(tuple_data[2:4:])
print(tuple_data[::-1])

"""

# append the data in to tuple
tuple_data = (1, 20, "RNS")
new_data = tuple_data + ("Tech",)
print(new_data)





