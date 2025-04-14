# Open a file for writing
file = open("output.txt", "w")

# Define a list of strings
list_of_lines = ["Line1\n", "Line2\n", "Line3\n"]

# Write the list of strings to the file
file.writelines(list_of_lines)

# Close the file
file.close()
