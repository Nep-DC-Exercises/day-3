# You will implement a guess-the-number game where the player has to try guessing a secret number until he gets it right. For now, you will "hard code" the secret number to 5 (just set it to five like secret_number = 5). You will prompt the player to enter a number again and again, each time comparing his input to the secret number. To to that, you will need to write a while loop. If he guesses correctly, you will print "You win!", otherwise, you will prompt for a number again.

secret_number = 5
check = True
print("I am thinking of a number between 1 and 10.")


while check:

    guess = int(input("What's the number? >> "))

    if guess == secret_number:
        print("Yes! You win!")
        check = False
    else:
        print("Nope, try again.")
