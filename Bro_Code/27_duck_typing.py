class bird():
    def fly(self):
        print("Bird is flying.")
class airoplane():
    def fly(self):
        print("Airoplane is flying.")
def make_to_fly(obj):
    obj.fly()
a = airoplane()
b = bird()
a.fly()
b.fly()