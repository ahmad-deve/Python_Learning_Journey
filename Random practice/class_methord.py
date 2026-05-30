class company():
    s = 56
    @classmethod
    def co(cls):
        print(f"This is {cls.s}")
c = company()
c.s = 78
c.co()