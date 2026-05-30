class twoDvector():
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"this is the three D vector {self.i}i , {self.j}j")
class threeDvector(twoDvector):
    def __init__(self,  i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"this is the three D vector {self.i}i , {self.j}j and {self.k}k")
t = twoDvector(1,2)
t.show()
th = threeDvector(1,2,5)
th.show()