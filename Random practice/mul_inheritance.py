class father():
    def skill(self):
        print("He is know the driving.")
class mother():
    def cook(self):
        print("She is know the cooking.")
class child(father,mother):
    def play(self):
        print("He is know the playing.")
c = child()
c.skill()
c.cook()
c.play()