# a function is a block of code which only runs when it is invoked

"""
return_val = print("Hello, How are you, Welcome")

print(return_val)

msg = "Welcome to python functions"
len_msg = len(msg)
print(len_msg)

def greet():
    print("Hello, How are you")
    print("Welcome to python functions")

greet()

# adding arguments
def get_average(input_numbers):
    sum_of_num = 0
    for num in input_numbers:
        sum_of_num += num
    avg = sum_of_num / len(input_numbers)
    print(avg)

my_list = [4, 8, 10, 20]
input_list = [1, 3, 5, 6]

get_average(my_list)
get_average(input_list)
get_average([1])

# positional based arguments
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter = counter + 1
    print("Number of times",  letter, " is ", str(counter))

print_letter_count("Welcome", "e")

# Parameters with name
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter = counter + 1
    print("Number of times",  letter, " is ", str(counter))

print_letter_count(text="Welcome", letter="e")
print_letter_count(letter="e", text="Welcome")

# parameters with default values
def print_letter_count(letter, text="Welcome"):
    counter = 0
    for char in text:
        if char == letter:
            counter = counter + 1
    print("Number of times",  letter, " is ", str(counter))

print_letter_count('e')
print_letter_count('t')
print_letter_count('m')
print_letter_count('t', "welcome to python functions")

#static based positional arguments
result = sum((1, 2, 3, 4, 5))
print(result)

#static based positional arguments
def mysum(a, b, c, d):
    print(a + b + c + d)

mysum(1,2,3,4)
mysum(1,2,3, 4, 5)

#dynamic based positional arguments

def mysum(*args):
    print(sum(args))

mysum()
mysum(1, 2, 3)
mysum(1, 2, 3, 4)
mysum(1, 2, 3, 4, 5)

"""
#key word based arguments

def key_values_func(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs)
    print(kwargs["name"])


key_values_func(name="rnstech", salary=20000, age=12)
key_values_func(name="rnstech", salary=20000, age=12, address="hyd")


