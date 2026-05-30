class car:
    def __init__(self,color,model,for_sale):
        self.color = color
        self.model = model
        self.for_sale = for_sale
    def car2special(self):
        print(f"You car color is {self.color}.")
        
car1 = car("red",2000,False)
print(car1.color)
car1.car2special()