def arrange_strings(string):
    reverse = string[::-1]
    result = [f'{i+1}: {reverse[i]}' for i in range(len(reverse))]
    return ', '.join(result)

string = input("Please provide strings").split()
print(arrange_strings(string))

s = 'Subin'
chars = list(s)
print(chars)