# L05-T2: Function with parameters, value comparison 

num1 = int(input('Enter the first integer:\n'))
num2 = int(input('Enter the second integer:\n'))

# function take two args num1, num2 compares and returns the larger value
def compare_numbers(num1, num2):
    if num1 > num2:
        print(f'{num1} is greater than {num2}')
        return num1
    elif num2 > num1:
        print(f'{num2} is greater than {num1}')
        return num2
    else:
        print('The integers are the same.')
        return num1 # if tie, return any num1 or num2

# calling the function to get the larger number
larger_num = compare_numbers(num1, num2)

new_num = int(input('Enter the integer that is subtracted from the larger:\n'))


number_after_subtraction = larger_num - new_num

# conditional expression to get the smaller number 
smaller_num = num1 if num1 < num2 else num2

if number_after_subtraction > smaller_num:
    print(f'{number_after_subtraction} is greater than {smaller_num}')
elif number_after_subtraction < smaller_num:
    print(f'{number_after_subtraction} is smaller than {smaller_num}')
else:
    print('The integers are the same')
