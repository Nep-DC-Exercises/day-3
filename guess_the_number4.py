# Limit the number of guesses the player has to 5. If he cannot guess the number within 5 guesses, he losses. Give the player the option to play again.
import random

secret_number = random.randint(1, 10)
check = True
limit = 5
print("I am thinking of a number between 1 and 10.")


while check:

    if limit > 0:

        guess = int(input("What's the number? >> "))

        if guess == secret_number:

            print("Yes! You win!")
            replay = input("Do you want to play again? Yes or No >>  ")
            replay.lower()

            if replay == "y" or "yes" or "yeah" or "yea":
                check = True
                limit = 5  # reset guesses
                # reset the number so it's not the same as the previous round
                secret_number = random.randint(1, 10)
            else:
                check = False

        elif guess > secret_number:
            print(f"{guess} is too high.")

        else:
            print(f"{guess} is too low.")

        limit -= 1

        if limit == 0:  # if this isn't here, at the end of the game, the user will see "You have 0 guesses remaining and "You ran out of guesses!" I think one message is enough.
            pass

        else:
            print(f"You have {limit} guesses remaining.")

    else:
        print("You ran out of guesses!")
        replay = input("Do you want to play again? Yes or No >>  ")
        replay.lower()
        if replay == "y" or "yes" or "yeah" or "yea":
            check = True
            limit = 5  # reset guesses
            # reset the number so it's not the same as the previous round
            secret_number = random.randint(1, 10)
        else:
            check = False
