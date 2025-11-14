# Prompt the user and store the input in the variable `number`
number = input("Enter a number to see its multiplication table:")

# Convert the input to an integer (so we can do arithmetic)
number = int(number)

# Use a for loop to print the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")


# Num = input("enter a number you wnat to see its multiplication table::")

# Num = int(Num)

# for x in range(1,20):
#         print(f"{Num} * {x} = {Num * x}")

