# Print a triangle consisting of * characters

star = "*"
star_mult = 1
height = 4
num_spaces = height - 1
i = 0

while i < height:
    if i == 3:
        print(star * star_mult)
    else:
        print(num_spaces * " " + (star * star_mult) + num_spaces * " ")

    i += 1
    star_mult += 2
    num_spaces -= 1
