class company():
    def __init__(self):
        print("this is the company.")
    a = 1
class employee(company):
    def __init__(self):
        print("this is the employess.")
    b = 2
class manager(employee):
    def __init__(self):
        super().__init__()
        print("this is the manager.")
    c = 3
m = manager()
print(m.c, m.b)