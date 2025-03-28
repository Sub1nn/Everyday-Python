#L06-T2: Removing duplicate elements from a list
integers = input('Give integers separated by commas\n')

# convert the comma-separated string into a list of integers
original_list = list(map(int, integers.split(',')))
print('Original List: ', original_list)

dup_list = []

for int in original_list:
    if int not in dup_list:
        dup_list.append(int)

print('List with duplicates removed: ', dup_list)
