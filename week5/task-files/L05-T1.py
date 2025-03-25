# L05-T1: Three different simple versions of a function

def print_lines():
    print('This is printed inside the function')

print_lines() # calling the function

number = int(input('Enter a number:\n'))

print(f'The input number is {number}')

def process_number(num): # function taking an argument
    print(f'The number squared is {number * number}')

process_number(number)


first_name = input('Enter your first name:\n')
last_name = input('Enter your last name:\n')

def print_whole_name(a,b): # function taking multiple arguments
    print(f'The full name is {first_name} {last_name}')

print_whole_name(first_name, last_name)
