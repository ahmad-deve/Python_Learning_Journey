def stair(n):
    if n == 0:
        print("All Done!")
    else:
        print("step: " , n)
        stair(n-1)
        print("step: " , n)
stair(8)