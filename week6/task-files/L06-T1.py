#L06-T1: Reversed list without using reverse() method or slicing
integers = input('Give integers separated by commas\n')

# convert the comma-separated string into a list of integers

integers_list = list(map(int, integers.split(',')))

reversed_list = []

# every iteration the integer is inserted at 0th index, reversing the list
for int in integers_list:
    reversed_list.insert(0, int)

print("Reversed list:", reversed_list)
