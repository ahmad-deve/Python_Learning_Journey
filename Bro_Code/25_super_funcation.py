class shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled
    def describe(self):
        print(f"This color is {self.color} and {'filled' if self.filled else 'not filled'}")
class circle(shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width = width
class triangle(shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width = width
        self.height = height
result_circle = circle(color="red",filled="Ture",width="23")
print(result_circle.color)
print(result_circle.filled)
print(result_circle.width)
result_circle.describe()