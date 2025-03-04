num = int(input("Giv an integer.\n"))

def factorial (num):
    if num < 1:
        return num
    
    sum = 1

    for i in range(1, num+1):
        sum = sum * i
    return sum

print(factorial(num))