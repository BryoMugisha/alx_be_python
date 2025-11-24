size = int(input("Enter a positive integer for the square size: "))


for i in range(size):            # outer loop for each row
    for j in range(size):        # inner loop for each column
        print("*", end="")       # print asterisk without newline
    print()                      # move to the next line after each row
