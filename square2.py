# Print a NxN square of * characters. Prompt the user for N.

counter = 0
lines = int(input("How big is the square? > "))

while counter < lines:
    print("*****")
    counter += 1
