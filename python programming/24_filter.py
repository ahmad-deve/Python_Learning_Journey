def is_even(a):
    return a % 2 == 0
number = [1,2,4,5,6,65,46,43,23]
even = filter(is_even,number)
print(list(even))