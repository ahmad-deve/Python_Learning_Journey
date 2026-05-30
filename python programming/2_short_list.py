number = [8,5,7,4,3,2,1,89]

for i in range(len(number)):
    for j in range(len(number)-i-1):
        if number[j]  > number [j+1]:
            number[j],number[j+1]  = number[j+1] , number[j]
print(number)