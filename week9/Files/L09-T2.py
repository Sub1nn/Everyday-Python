def read_integers_from_file(filename):
    """
    Reads integers from a file, one per line, into a list.
    Catches and handles file-related exceptions.
    """
    # L09-T2-file-handle: Begin file read
    numbers = []
    try:
        file = open(filename, 'r')  # Explicitly open the file
        for line in file:
            line = line.strip()
            if line.isdigit():
                numbers.append(int(line))
            else:
                raise ValueError("Non-integer value found in file.")
        
        # Check if the file was empty
        if not numbers:
            raise ValueError("File is empty or has no valid integers.")
        
        file.close()  # Explicitly close the file
        return numbers
    except (FileNotFoundError, IOError, ValueError):
        # L09-T2-file-handle: Error during file read
        return None  # Return None to indicate an error
    finally:
        try:
            file.close()  # Attempt to close if it was opened
        except:
            pass
    # L09-T2-file-handle: End file read


def write_integers_to_file(numbers, filename):
    """
    Writes a list of integers to a file, one per line.
    Catches and handles file-related exceptions.
    """
    # L09-T2-file-handle: Begin file write
    try:
        file = open(filename, 'w')  # Explicitly open the file
        for number in numbers:
            file.write(f"{number}\n")
        
        file.close()  # Explicitly close the file
        return True  # Return True to indicate success
    except (IOError, PermissionError):
        # L09-T2-file-handle: Error during file write
        return False  # Return False to indicate an error
    finally:
        try:
            file.close()  # Attempt to close if it was opened
        except:
            pass
    # L09-T2-file-handle: End file write


def main():
    # Prompt for the input file name
    input_filename = input("Enter the name of the file to be read:\n").strip()
    
    # Check for empty input
    if not input_filename:
        print(f"Error processing file '{input_filename}'.")
        return

    numbers = read_integers_from_file(input_filename)
    
    # Check if reading failed
    if numbers is None:
        print(f"Error processing file '{input_filename}'.")
        return

    # Confirm the file was read successfully
    print(f"File '{input_filename}' read successfully, {len(numbers)} lines.")

    # Prompt for the output file name
    output_filename = input("Enter the name of the file to be written:\n").strip()
    
    # Check for empty output filename
    if not output_filename:
        print(f"Error processing file '{output_filename}'.")
        return

    success = write_integers_to_file(numbers, output_filename)
    
    # Check if writing failed
    if not success:
        print(f"Error processing file '{output_filename}'.")
    else:
        print(f"File '{output_filename}' was successfully written.")


# Run the main program
if __name__ == "__main__":
    main()
