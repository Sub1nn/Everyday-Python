#L07-T2: Copying from one file to another

def file_copy(fileA, fileB):
    # Open the source file for reading
    source_file = open(fileA, 'r')
    # Open the destination file for writing (creating it if it doesn’t exist)
    destination_file = open(fileB, 'w')
    try:
        # Read contents from the source and write to the destination
        for line in source_file:
            destination_file.write(line)
    finally:
        # Close both files explicitly
        source_file.close()
        destination_file.close()


def main():
    # Ask for the source and destination file names
    source = input("Please give the name of the source file:\n")
    destination = input("Please give the name of the destination file:\n")
    
    # Call the file copy function
    file_copy(source, destination)
    
    # Confirm successful copying
    print("File copied successfully!")


# Run the main function
main()
