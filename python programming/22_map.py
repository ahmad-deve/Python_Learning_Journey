# without map funcation
number = [1,2,3,4,5]
result = []
for n in number:
    result.append(n*n)
print(result)

# with map funcation
def square(n):
    return n*n
number = [1,2,3,4,5]
dou = map(square,number)
# print(dou)