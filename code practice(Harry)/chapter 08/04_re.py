def re(n):
    if(n==1 or n==0):
        return 1
    return n *re(n-1)

n = int(input("Enter the inpute: "))
print(f"The for of the enter number is {re(n)}")

# #Funcation Defication
# def goodday():
#     print("Good Day")

# goodday()  #Funcation Call


# def gd(name, ending="thank you"): # default value  + parameter
#     print("Good Day," + name)
#     print(ending)

# gd("ahmad", "not you are late")   # Funcation call