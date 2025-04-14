file = open("Example.txt", "r")
line = file.readline().strip()
while line != "":
    print(line)
    line = file.readline().strip()
file.close()
    
