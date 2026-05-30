attempt = 1
max_attempt = 3
while attempt <= max_attempt:
    password = input("Enter the password: ")
    if password == "@mala11840":
        print("Now, We can move the next step>")
        break
    else:
        print("you enter the wrong password.")
        attempt +=1
    if attempt == max_attempt:
        print("your account is locked.")
        break