# Make blastoff wait one second before proceeding to the next number

import time

i = int(input("Enter the number to start counting from. >> "))

if i <= 20:
    while i >= 0:
        print(i)
        time.sleep(1)
        i -= 1
else:
    print("That number was too high. It can't be larger than 20.")
