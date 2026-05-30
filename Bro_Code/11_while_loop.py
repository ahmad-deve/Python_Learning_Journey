user_input_name = input("Enter your name: ")
while user_input_name == "":
    print("You didn't not enter your name.")
    user_input_name = input("Enter your name: ")
print(f"Welcome {user_input_name}")
