# Read file content called test.txt
# and print it to the console

# Open file
file = open("test.txt", "r")

# Read file content
content: str = file.read()
calories_array: list[list[str]] = []
buffer: list[str] = []

for calories in content.split("\n"):
    buffer.append(calories)
    if len(calories.strip()) == 0:
       # if buffer is empty, skip
        if len(buffer) == 0:
           continue
        else:
            calories_array.append(buffer)
            buffer = []
    print(buffer)
# Print content
#print(content)

# Close file
file.close()
