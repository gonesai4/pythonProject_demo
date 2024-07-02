# Modules
#   - reusing the code
#         - same project
#         - other projects
#         - other globally
#   - decomposing the code

# 2 ways modules
#   - default modules (python library)
#   - custom modules

"""
# Default Modules

import math

print(math.floor(3.6))
print(math.ceil(3.6))
print(math.trunc(3.6))

# 3! = 3 * 2 * 1 = 6
# 5! = 5 * 4 * 3 * 2 * 1 = 120

print(math.factorial(3))
print(math.factorial(5))

# printing all the math related functions from math module directory
# printing all the math related functions from math module
import math
for name in dir(math):
    print(name)

# using multiple modules
import math, sys
for name in dir(sys):
    print(name)

print("before exit statement")
sys.exit()      # exiting the process here
print("after exit statement")

import platform

print(platform.architecture())
print(platform.system())
print(platform.python_version())
print(platform.uname())


# generating/picking up random values
import random

print(random.random())

numbers = [1, 2, 3, 4, 5, 6]
skills = ["DevOps", "AWS", "Python", "AI", "MLOps"]

print(random.choice(numbers))
print(random.sample(skills, 3))


# importing only particular modules
from random import random, choice, sample

print(random())

numbers = [1, 2, 3, 4, 5, 6]
skills = ["DevOps", "AWS", "Python", "AI", "MLOps"]

print(choice(numbers))
print(sample(skills, 2))

# using alias names if module name is big


import sys as s

print("before exit statement")
s.exit()      # exiting the process here
print("after exit statement")



import sys
# Over riding default modules with custom modules
# first it will take prior to local/custom module then default moduls
from random import random, choice, sample
from sys import exit

print(random())

numbers = [1, 2, 3, 4, 5, 6]
skills = ["DevOps", "AWS", "Python", "AI", "MLOps"]

print(choice(numbers))
print(sample(skills, 2))

def exit():
    print("I want exit")

print("before exit statement")
exit()      # exiting the process here
print("after exit statement")

"""




