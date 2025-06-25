import math
import random
import string

def generate_pass():
    LETTERS = string.ascii_letters
    DIGITS = string.digits
    SPECIAL = string.punctuation
    COMB = LETTERS + DIGITS + SPECIAL

    random.seed(8292)
    
    while True:
            length = int(input("Enter the length of the password:\n"))
            if length <= 0:
                print("Password length must be a positive integer.")
            else:
                #: using generator expression
                password = "".join(random.choice(COMB) for choice in range(length))
                print(f"Generated password: {password}")
                break



generate_pass()

# Alternative using list comprehenson
# Generate password as a list of random characters
password_list = [random.choice(COMB) for _ in range(length)]

password = ''.join(password_list)  # This creates a continuous string from list elements
