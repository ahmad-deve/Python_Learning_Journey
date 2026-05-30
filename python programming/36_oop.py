try:
    class house:
        def __init__(self,location,price):
            self.location = location
            self.price = price
    loc = input("Enter the house location: ")
    pri = int(input("Enter the house price: "))
    my_house = house(loc,pri)
    print(f"This house is located in {my_house.location} and the price is {my_house.price}.")
except Exception as e:
    print(f"you enter invalid input: {e}")