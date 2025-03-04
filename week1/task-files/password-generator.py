import random

password_length = int(input("Enter the password length: "))
password = ""


lowercase_letters = "abcdefghijklmonpqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

digits = "0123456789"
symbols = "!@#$^&*()_-+"

characters = lowercase_letters + uppercase_letters + digits + symbols

for i in range(password_length):
    password += random.choice(characters)

print("Generated Password:", password)
