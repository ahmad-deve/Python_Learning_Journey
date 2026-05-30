class animal():
    def speak(self):
        pass
class cat(animal):
    def speak(self):
        print("MENO")
class dog(animal):
    def speak(self):
        print("Bark")
class car:
    def speak(self):
        print("Honk")
animals = [cat(),dog(),car()]
for animal in animals:
    animal.speak()