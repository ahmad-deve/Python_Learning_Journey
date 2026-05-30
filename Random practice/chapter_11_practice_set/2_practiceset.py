class animal():
    pass
class pet(animal):
    pass
class dog(pet):
    @staticmethod
    def bark():
        print("Bow Bow")
d = dog()
d.bark()