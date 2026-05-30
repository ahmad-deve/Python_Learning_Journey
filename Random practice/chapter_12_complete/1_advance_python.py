# using walrus operator
if (n := len([1,2])) > 3:
    print (f"List i stoo long ({n} elements, experted <=3)") # output: list is too long ( 5 elements, expected <= 3)
else:
    print(f"the list is too short {n} in the element.")