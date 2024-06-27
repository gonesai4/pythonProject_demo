# Handling error using Exception block
"""

try:
    data = {"A": 1, "B": 2}
    print(data["C"])
    print(10/0)
except:
    print("Exception in Code")
finally:
    print("Finally block")

"""

# Handling error based exceptions

try:
    data = {"A": 1, "B": 2}
    print(data["A"])
    print(10/0)
except KeyError:
    print("There is no such key in the dictionary, Please check the key")
except ZeroDivisionError:
    print("We should not do division with zero")
except:
    print("There is some error, please check it.")
finally:
    print("Successfully Processed")



