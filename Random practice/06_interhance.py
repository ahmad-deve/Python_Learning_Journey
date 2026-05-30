class company:
    company_name = "Google"

    def show(self):
        print(f"show the {self.language} and his name is {self.name}")
    
class programming(company):
    company_name = "Amazon"

    def show_salarry(self):
        print(f"show the {self.salaary} and his name is {self.name}")

a = company()
b = programming()

print(a.company_name,b.company_name)