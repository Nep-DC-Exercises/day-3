# Make sure user doesn't enter a number larger than 20

i = int(input("Enter the number to start counting from. >> "))

if i <= 20:
    while i >= 0:
        print(i)
        i -= 1
else:
    print("That number was too high. It can't be larger than 20.")
