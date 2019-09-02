# Improve your game to provide the player with a high-or-low hint.

secret_number = 5
check = True
print("I am thinking of a number between 1 and 10.")


while check:

    guess = int(input("What's the number? >> "))

    if guess == secret_number:
        print("Yes! You win!")
        check = False
    elif guess > secret_number:
        print(f"{guess} is too high.")
    else:
        print(f"{guess} is too low.")
