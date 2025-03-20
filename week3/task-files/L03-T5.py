# L03-T5: String Comparison and Palindrome Testing
# Comparing two words, checking if word has 'Z', and testing for a palindrome.

# Asking user for two words
word1 = input("Enter word 1:\n")
word2 = input("Enter word 2:\n")

# String comparison
if word1 > word2:
    print(f"'{word2}' comes earlier in order than '{word1}'.")
elif word1 < word2:
    print(f"'{word1}' comes earlier in order than '{word2}'.")
else:
    print("The words are the same.")
    
# Checking if "z" is in either word
if "z" in word1:
    print(f"Letter 'z' is found in word '{word1}'.")
if "z" in word2:
    print(f"Letter 'z' is found in word '{word2}'.")
if "z" not in word1 and "z" not in word2:
    print("The letter 'z' was not found in either of the words.")

# Palindrome testing
is_palindrome = input("Enter a word to be tested:\n")

# Reversing the input to check for palindrome
if is_palindrome == is_palindrome[::-1]:
    print(f"'{is_palindrome}' is a palindrome.")
else:
    print(f"'{is_palindrome}' is not a palindrome.")
