class animal():
    def eat(self):
        print("Animal are eating the meet.")
class dog(animal):
    pass
class cat(animal):
    pass
d = dog()
c = cat()
d.eat()
c.eat()