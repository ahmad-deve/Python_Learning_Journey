class car:
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed
    @classmethod
    def car_info(cls,color,speed):
        return cls(color , speed)
    @staticmethod
    def car_about():
        print("This is the super car his color is red")
my_car = car.car_info("red","400km")
print(my_car.color)
print(my_car.speed)
car.car_about()