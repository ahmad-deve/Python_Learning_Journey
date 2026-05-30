def dragen(n):      #funcation defnation
    if n == 0 :     # base case
        print("The Dragen health is 0 and he is died.Now!")     # what print when the if statement is become ture.
    else:   # what execute when the if statement not match.
        print("Dragen Health: " , n) # print when the else is execute.
        dragen(n-1)     # Recursion case
hel = int(input("Enter the Dragen Health: "))       # input the health of the Dragen
dragen(hel) # funcation call 