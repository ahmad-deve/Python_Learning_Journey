class pray:
    def no_hunt(self):
        print("this is not a hunter.")
class pre:
    def hunter(self):
        print("this can be hunt.")
class lion(pre):
    pass
class rabbit(pray):
    pass
class hen(pray,pre):
    pass
class spprow(pray):
    pass

Rabbit = rabbit()
Rabbit.no_hunt()
Hen = hen()
Hen.no_hunt()