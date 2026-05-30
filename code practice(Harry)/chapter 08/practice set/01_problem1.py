def greatest(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c 
    
a = 32
b = 2
c = 7
print(f"The greatest number is {greatest(a,b,c)}")