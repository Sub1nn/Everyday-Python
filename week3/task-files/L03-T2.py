# L03-T2: String Comparison with Multiple Conditions
# Check if the user wants to exit or continue with the login.

while True:
    stop = input("Do you want to stop the execution of the program (Y/N):\n").upper()
    if stop == 'Y':
        print("Bye!")  # Exiting the program
        break
    elif stop == 'N':
        username = input("Enter username:\n")  # User input for username
        password = input("Enter password:\n")  # User input for password
        if username == "Pekka" and password == "somerandomthing":
            print("User recognized!")  # login the user
            break
        else:
            print(f"You entered an invalid login name or password.\nName length: {len(username)}")
    else:
        print("Invalid input! Please try again.")  # In case of invalid input
