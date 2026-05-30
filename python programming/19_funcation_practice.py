prcie_per_item = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
def total_cost(prcie_per_item,quantity):
    print(f"You order the pizza and pizza cost is: {prcie_per_item}.\nYou order the quantity: {quantity}.")
    return prcie_per_item*quantity
    
total = total_cost(prcie_per_item,quantity)
print(f"the total cost is {total}")