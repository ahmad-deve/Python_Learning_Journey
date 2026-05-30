def discount(orignal_price,discount_price):
    return orignal_price - (orignal_price*discount_price/100)
ori = int(input("Enter the orignal price: "))
dis = int(input("Enter the discount_price price: "))
res = discount(ori,dis)
print(f"dicount price: {res}")