def temp_convet(cel):
    return (cel *9/5)+32
number = [65,89,75,15]
conveted = list(map(temp_convet,number))
print(conveted)