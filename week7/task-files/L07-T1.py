#L07-T1

def file_write(name):
    # Open the file in write mode to clear previous contents
    file = open(name, 'w')
    try:
        while True:
            name_input = input("Enter a name to save to the file (0 to stop):\n")
            if name_input == '0':
                break
            # Write the input name to the file with a newline
            file.write(name_input + '\n')
    finally:
        # Close the file explicitly within a 'finally' block
        file.close()


def file_read(name):
    # Open the file in read mode
    file = open(name, 'r')
    try:
        print(f"The following names are stored in the file '{name}':")
        for line in file:
            # Print each line without additional newline characters
            print(line.strip())
    finally:
        # Close the file explicitly
        file.close()


def main():
    # Ask for the filename from the user
    filename = input("Enter the name of the file to be saved:\n")
    file_write(filename)
    file_read(filename)


# Run the main function
main()
