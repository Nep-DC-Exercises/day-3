# Print the first 100 triangle numbers.

i = 1

while i <= 100:
    triangle_number = int((i * (i + 1)) / 2)
    print(f"Triangle #{i} is {triangle_number}.")
    i += 1
