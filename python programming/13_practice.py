# try and except the program 
try:
    user_name = int(input("Enter the number: "))
    print(f"You enter the number {user_name}.")
    if user_name >= 45:
        print("Enter the above number")
    elif user_name >= 55:
        print("Enter the above number of 55")
    else:
        print("you lose the game.")
except:
 print("unvalid the input.")