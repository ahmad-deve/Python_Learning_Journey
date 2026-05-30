# username can't contain the 12 char long
# username can't contain the space's
# username can't contain the numbers

user_input = input("Enter your username: ")
if len(user_input) > 12:
    print("username didn't contain the more than 12 characters.")
elif not user_input.find(" "):
    print("username didn't cotain the spaces")
elif not user_input.isalpha():
    print("username didn't  contain the numbers")
else:
    print(f"Welcome {user_input}")