# A loop with in another loop.
# outer loop:
    # inner loop:
user_intput = int(input("Enter the number: "))
for i in range(1,user_intput):
    for j in range(i):
        print("*",end="")
    print()
