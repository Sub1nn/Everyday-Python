# L04-T3: Repetition structure with multiple termination conditions

a = int(input('Enter a:\n'))
b = int(input('Enter b:\n'))

while a <= 1000 and b <= 1000:
    print(f'a: {a} b: {b}')
    a = a * 2
    b = b + 100

# check the reason that ended the loop after exiting the loop
if a > 1000 and b > 1000:
    print('a exceeded 1000')
    print('b exceeded 1000')
elif a > 1000:
    print('a exceeded 1000')
elif b > 1000:
    print('b exceeded 1000')
