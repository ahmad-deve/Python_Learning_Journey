class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def detail(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old. i am in grade {self.grade}")

    def get_name(self):
        print(f"My name is {self.name}")

student_1 = student("ALi",20, 89)
student_1.detail()

student_2 = student("ahmad",23, 78)
student_2.get_name()