p1 = "buy now"
p2 = "make money"
p3 = "click here"

message = input("Write your comment here: ")

if ((p1 in message) or (p2 in message) or (p3 in message)):
    print("This is spam comment. \n we can't proceed more.(block here)",)

else:
    print("yah!\nwe can process more.This comment is not spam.")