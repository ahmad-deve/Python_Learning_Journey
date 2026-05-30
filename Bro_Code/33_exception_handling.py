try:
    number_input = int(input("Enter the Number:"))
    print(f"You enter the number: {number_input}.")
    result = number_input/2
    print(f"After the division by 2 the answer is : {result}.")
except ZeroDivisionError:
    print("You can't division by zero.")
except ValueError:
    print("Kindly! enter the number.")
finally:
    print("Clean up here! ")