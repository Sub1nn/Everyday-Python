# L04-T2: Repetition structure with string

word = input('Enter a string:\n')

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

count = 0

for char in word:
    if char in vowels: # check if character is a vowel
        count+=1
        
print(f'Number of vowels is: {count}')
