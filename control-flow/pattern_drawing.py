# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Start with the first row
row = 0

# While loop controls the rows
while row < size:
    # For loop prints stars on the same line
    for col in range(size):
        print("*", end="")

    # After printing each row, move to the next line
    print()

    # Move to the next row
    row += 1
