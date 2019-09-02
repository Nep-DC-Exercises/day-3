# Print the multiplication table for numbers from 1 up to 10.

first_num = 1
second_num = 1


while first_num <= 10:

    while second_num <= 10:

        result = first_num * second_num
        print(f"{first_num} x {second_num} = {result}")
        second_num += 1

    first_num += 1
    second_num = 1
