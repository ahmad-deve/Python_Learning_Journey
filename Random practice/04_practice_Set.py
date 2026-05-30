class  demo():
    a = 4
    

o = demo()  # attribute is change 
print(o.a)
demo.a = 2  # instance is set that why
o = demo()
print(demo.a)  # the print the class attribite


