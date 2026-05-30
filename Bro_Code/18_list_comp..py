# list comprehension: and correct an dgaster way to list the list  
# formula: expression for while value in interable if condition

lis = [1,2,3,4,5]
# new_lis = [n*3 for n in lis]
# new_lis = [n*3 for n in lis if n % 2 == 0]
new_lis = ["even" if n % 2 == 0 else "odd" for n in lis]
print(new_lis)


# odd_nums = [num for num in range(1, 11) if num % 2 != 0]

result = []
for i in range(5):
    if i % 2 == 0:
        result.append(i)
print(result)


five = [num for num in range(6) if num % 2 == 0]
print(five)

big = [10,2,8,1]
new_big = ["big" if n > 5 else "small" for n in big]
print(new_big)