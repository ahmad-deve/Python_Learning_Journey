class cal:
    def __init__(self, n):
        self.n = n

    def squ(self):
        print (f"the squ is {self.n*self.n}")
    def cube(self):
        print (f"the cube is {self.n*self.n*self.n}")
    def squroot(self):
        print (f"the squroot is {self.n**1/2}")

    @staticmethod
    def hell():
        print("Hello Word!")


r = cal(4)
r.hell()
r.cube()
r.squ()
r.squroot()