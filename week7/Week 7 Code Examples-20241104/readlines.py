file = open("Example.txt", "r")
lines = file.readlines()

stripped_lines = []

# Iterate over each line and strip whitespace
for line in lines:
    stripped_lines.append(line.strip())

# Print the stripped lines
for line in stripped_lines:
    print(line)

file.close()


    
    

    
