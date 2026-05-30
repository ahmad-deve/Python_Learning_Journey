class grand_father():
    def house(self):
        print("He is own the house.")
class father(grand_father):
    def car(self):
        print("He is own the car.")
class son(father):
    def bike(self):
        print("He is own the bike.")
now = son()
now.house()
now.car()
now.bike()