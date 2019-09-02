# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.

start_num = int(input('Start Number: '))
end_num = int(input('End Number: '))


while start_num < end_num + 1:
    print(start_num)
    start_num += 1
