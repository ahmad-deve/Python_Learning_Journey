marks = {
    "ahmad": 100,
    "ali" : 52,
    "ameen" :26,
}

print(marks.keys())
print(marks.items())
print(marks.values())
# print(marks.update{"ali" = 100})

# print(marks)

print(marks.get("ali2"))  # print none if dont exiest 

print(marks["ali"])  # return an error if not 