class student:
    def __init__(self,name: str,grade: int,iq: float):
        self.name = name
        self.grade = grade
        self.iq = iq

    def about(self):
        print(f"This student name is {self.name}.He is reading the grade {self.grade} and this student have the iq is {self.iq}.")

    @staticmethord
    def info():
        print(f"the is the static methord by created the ")

stu1 = student("Ahmad",9,7.3)
print(stu1.name, stu1.grade, stu1.iq, stu1.about())

info()