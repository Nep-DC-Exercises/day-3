# Prompt: Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string.

user_string = input("Insert your text here. >> ")
star = "*"
i = 0
border_length = len(user_string) + 4
border = star * border_length

while i < 3:

    if i == 1:  # print a star and then the text
        print(f"{star} {user_string} {star}")

    else:
        print(f"{border}")

    i += 1
