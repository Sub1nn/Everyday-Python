start_num = int(input('Enter the starting value:\n'))
end_num = int(input('Enter the ending value:\n'))

for num in range(start_num, end_num+1): # range() function does not include the upper bound, so have to do (+1)
    print(num)
