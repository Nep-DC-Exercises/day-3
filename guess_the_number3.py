# Instead of hard-coding the secret number to 5 now, you will generate the secret number using a random number generator provided by Python, so that even you, the programmer, cannot know the secret number before hand.
import random

secret_number = random.randint(1, 10)
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
