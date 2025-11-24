number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to generate the table from 1 to 10
for X in range(1, 11):
    Z = number * X
    print(f"{number} * {X} = {Z}")
