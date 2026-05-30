class student():
    @property
    def name(self):
        return f"The name you write is the: {self.fname} \nThe profession is: {self.pname}"
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.pname = value.split(" ")[1]
e = student()
e.name = "Ahmad MLEngineer"
print(e.name,e.pname)
