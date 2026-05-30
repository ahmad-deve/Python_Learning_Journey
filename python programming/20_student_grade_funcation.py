def grade_system(grade):
    if grade >= 90 and  grade <=100:
        print("your grade is A.")
    elif grade >= 80 and grade <= 89:
        print("your grade is B.")
    elif grade >= 70 and grade <= 79:
        print("your grade is C.")
    elif grade >= 60 and grade <=69:
        print("your grade is B.")
    else:
        print("below 60")
grad = int(input("Enter your grade: "))
re = grade_system(grad)
