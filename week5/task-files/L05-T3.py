# L05-T3: Function with parameters, string check

# Input strings from the user
first_str = input('Enter the first string:\n')
second_str = input('Enter the second string:\n')

# Function to check if the first string is contained in the second string
def is_substring(str1, str2):
    # If the first string is longer, it can't be a substring of the second string
    if len(str1) > len(str2):
        return False

    # Loop through the second string to find the first string as a substring
    for i in range(len(str2) - len(str1) + 1):
        match = True

        # Check each character of str1 against the corresponding position in str2
        for j in range(len(str1)):
            if str2[i + j] != str1[j]:
                match = False
                break

        if match:
            return True  # Return True if a match is found

    return False  # Return False if no match is found

# Call the function and store the result
result = is_substring(first_str, second_str)

# Print the appropriate message based on the result
if result:
    print('The first string can be found in the second string.')
else:
    print('The first string cannot be found in the second string.')
