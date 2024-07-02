"""
list_utils.py is a sample python module that exposes list utility functions

__usage_counter variable is private/local variable, we can use this only within the module
we can not use this in outside module.

"""
__usage_counter = 0

def sum_elements(user_list):
    global __usage_counter
    __usage_counter += 1
    element_sum = 0
    for el in user_list:
        element_sum += el
    return element_sum


def double_each_element(user_list):
    global __usage_counter
    __usage_counter += 1
    return [element * 2 for element in user_list]



def get_usage_counter():
    global __usage_counter
    return __usage_counter


if __name__ == '__main__':
    entry_list = [1, 2, 3, 4, 5]
    summed = sum_elements(entry_list)
    # summed = sum_elements(entry_list)
    if summed == 15:
        print("Sum is okay")
    else:
        print("Sum is not okay")

    doubled = double_each_element(entry_list)
    entry_list =  doubled
    doubled = double_each_element(doubled)
    if doubled == [2, 4, 6, 8, 10]:
        print("Doubled is okay")
    else:
        print("Doubled is not okay")
    print("The counter value - " + str(__usage_counter))
