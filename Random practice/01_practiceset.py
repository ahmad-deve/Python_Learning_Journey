class microsoft:
    company = ["microsoft", "google", "amazon", "netflix"]
    def __init__(self, name , salary):
        self.name = name 
        self.salary = salary
      

a = microsoft("Ahmad", 150000)
print(f"The employee name is {a.name} and salary is {a.salary}.He is the part of {a.company[3]}.")
h = microsoft("Hadi", 13000)
print(f"The employee name is {h.name} and salary is {h.salary}.He is the part of {h.company[2]}.")