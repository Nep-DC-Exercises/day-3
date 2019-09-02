# Modify blastoff so that it prints a custom message once it gets to 0

i = 10
message = "We have liftoff!"

while i >= 0:

    if i == 0:
        print(i)
        print(message)
    else:
        print(i)

    i -= 1
