# Given a number, print its factors.

factors = []
user_num = int(input("Enter a whole number >> "))

i = 1

while i <= user_num:

    if user_num % i == 0:

        if i not in factors:
            factors.append(i)
            factors.append(-i)

    i += 1


print(factors)
