foods = []
price = []
total = 0
while True:
    food_input = input("Enter the the food (q for quite): ")
    if food_input.lower() == "q":
        break
    else:
        food_price = int(input("Enter the food price : $"))
        foods.append(food_input)
        price.append(food_price)
for food in foods:
    print(food)
for prices in price:
    total += prices
print(f'your total is ${total}.')