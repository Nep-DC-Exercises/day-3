# Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.

star = "*"
star_multiplier = 1
height = int(input("How high do you want the triangle to be? >> "))
# Space on each side of the "*" character in order to center the triangle
num_spaces = height - 1
i = 0

while i < height:  # prints a triangle top to bottom with spaces on each side
    if i == height - 1:
        print(star * star_multiplier)
    else:
        print(num_spaces * " " + (star * star_multiplier) + num_spaces * " ")

    i += 1
    star_multiplier += 2  # each layer of the triangle increases by 2 stars
    num_spaces -= 1  # as the triangle gets wider, we need less space on the sides
