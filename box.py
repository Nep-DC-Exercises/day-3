# Given a height and width, input by the user, print a box consisting of * characters as its border.

width = int(input("Enter width of box > "))
height = int(input("Enter height of box > "))
star = "*"
i = 0
mid = width - 2

while i < height:

    if i == 0:  # top of box
        print(width * star)

    elif i == height - 1:  # bottom of box
        print(width * star)

    elif i >= 1 or i < height - 1:  # middle rows of box
        print("*" + mid * " " + "*")

    i += 1
