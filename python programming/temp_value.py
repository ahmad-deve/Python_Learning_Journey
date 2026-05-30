def temp_value(temp_value,unit):
    if unit == "c":
        return(temp_value - 32)*5/9
    elif unit == "f":
        return(temp_value * 9/5) +32
    else:
        print("invalid number")
temp = float(input("Enter the temp number: "))
unit = (input("Enter the unit: "))
result = temp_value(temp,unit)
print(f"result:  {result}")