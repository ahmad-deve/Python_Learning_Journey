try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
except:
    pass
try:
    print("If you want to add the number press, 1")
    print("If you want to subtract the number press, 2")
    print("If you want to muiltply the number press, 3")
    print("If you want to divide the number press, 4")
    user_input = int(input("Enter the number: "))
    if user_input == 1:
        print(f"The sum of the {first_number} and {second_number} is {first_number+ second_number}")
    elif user_input ==2:
        print(f"The subtraction of the {first_number} and {second_number} is {first_number-second_number}")
    elif user_input ==3:
        print(f"The mul of the {first_number} and {second_number} is {first_number*second_number}")
    elif user_input ==4:
        print(f"The divide of the {first_number} and {second_number} is {first_number/second_number}")
    else:
        print("You enter the invalid number!")
except:
    print("You enter the invalid number!")