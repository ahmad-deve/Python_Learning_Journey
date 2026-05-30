try:
    user_input = int(input("Enter the number: "))
    print(f"You enter {user_input}")
except ValueError:
    print(f"you enter the invalid value error.")
except Exception as e:
    print(f"Error Oucrred: {e}.")
print(f"you enter the close the file")