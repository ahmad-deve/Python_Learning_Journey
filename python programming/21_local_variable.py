x = 10   # Global Variable 
def show():
    global x 
    x = 19  # Global Variable Chnage
    print(x)
show()  # Output 19