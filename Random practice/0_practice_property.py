class student():
    @property
    def name(self):
        return f"The name is {self.fname} \nThe profession is {self.pname}"
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.pname = value.split(" ")[1]
s = student()
s.name = ("Ahmad ML_Engineer")
print(s.name)
