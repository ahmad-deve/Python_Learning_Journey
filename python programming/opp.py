class Employee:
    name = "__ahmad"
    lass = 4

    def getinfo(self):
        print(f"his name is {self.name}. and he is earn even the less than {self.lass}$.")


Employee_1 = Employee()
Employee.name = "Hadi"
Employee_1.getinfo()