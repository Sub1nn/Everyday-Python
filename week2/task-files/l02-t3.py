long_word = input("Enter a long word:\n")
# Slicing the first 5 characters
first_five_letters = long_word[:5]
print(f"The first five letters are: {first_five_letters}")
# Slicing the last five letters
last_five_letters = long_word[-5:]
print(f"The last five letters are: {last_five_letters}")
# Slicing from second to fifth letters
second_to_fifth = long_word[1:5]
print(f"Letters 2, 3, 4, 5 are: {second_to_fifth}")
# using :: slices the string from start to end, and ::step slices with a
# step provided. In 1::2, 1 is the start index.
every_second_letter = long_word[1::2]
print(f"Every second letter of the word: {every_second_letter}")
# word[::-1] slices the string word from start to end, but with a step
# of -1, which effectively reverses the string.
word_backward = long_word[::-1]
print(f"The word backwards: '{word_backward}'")

start = int(input("Enter start index:\n"))
end = int(input("Enter end index:\n"))
step = int(input("Enter step:\n"))

final_output = long_word[start:end:step]
# len(string) gives the length of the string
length_final_output = len(final_output)

print(f"With these values '{long_word}' produces this: {final_output}")
print(f"Your word is {length_final_output} characters long")
