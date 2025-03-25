str1 = input("Enter first string:\n")
str2 = input("Enter second string:\n")

def get_substring(str1, str2):
    for i in str1:
        print(i)
        for j in str2:
            print(j)

get_substring(str1, str2)
