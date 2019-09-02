'''
Write a program that will prompt you for how many coins you want. 
Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. 
If you type no, it will stop the program. 
'''
coins = 0
counter = True

print(f"You have {coins} coins.")
answer = input("Do you want another? > ")

while counter:
    if answer == "yes":
        coins += 1
        print(f"You have {coins} coins.")
        answer = input("Do you want another? > ")
    else:
        print("Bye")
        break
