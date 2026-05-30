def io(n):
    if(n==0):  # base conditation
        return
    print("*" * n)
    io(n-1)

io(8)
# Extra not working:    
# n = int(input("Enter the number: "))
# print(f"{io(n)}")
# # io(n)