class student:  #bule print
    def __init__(self,name,age):       #def with init
        self.name = name        # Attribute in def
        self.age = age        # Attribute in def
    def about_student(self):    # Methords 
        print(f"The student name is {self.name}.\nHis age is {self.age}.")      # what methord will be print/output.
nam = input("Enter your name: ") 
ag = input("Enter your age: ")
student_data = student(nam,ag)
student_data.about_student()    #calling