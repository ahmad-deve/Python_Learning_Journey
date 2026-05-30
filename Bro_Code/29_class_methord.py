class student():
    count = 0
    total_cgpa = 0
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
        student.count += 1
        student.total_cgpa += cgpa
    def get_info(self,name,cgpa):
        return f"{self.name} {self.cgpa}"
    @classmethod
    def get_count(cls):
        return f"Total number of the student: {cls.count}."
    @classmethod
    def total_avg(cls):
        if cls.total_cgpa == 0 :
            return 0 
        else:
            return cls.total_cgpa/cls.count
student1 = student("Ahmad",3.4)
student2 = student("Ali",3.0)
print(student.get_count())
print(student.total_avg())