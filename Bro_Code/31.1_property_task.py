class student:
    def __init__(self,name,marks):
        self._name = name
        self._marks = marks
    @property
    def marks(self):
        return f"Name: {self._name} | Marks: {self._marks}"
    @marks.setter
    def marks(self,value):
        if value >= 0 and value <= 100:
            self._marks = value
        else:
            print( f"Invalid marks")
s = student("ALi",85)
s.marks = 95 
s.marks = 195
print(s.marks)