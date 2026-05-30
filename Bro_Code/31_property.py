class laptop:
    def __init__(self,company_name,stroage):
        self._company_name = company_name
        self._stroage = stroage
     
    @property
    def company_name(self):
        return f"company name is: {self._company_name} | Stroage is: {self._stroage} SSD"
    @property
    def stroage(self):
        return f"stroage: {self._stroage}"
    @stroage.setter
    def stroage(self,value):
        if (value>= 0):
            self._stroage = value
        else:
            print("Invalid input!")
com = laptop('hp',132)
# com.stroage = 100
print(com.company_name)