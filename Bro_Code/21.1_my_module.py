def greet(name):
    print(f"Good morning {name}")

def tax_information(all_money, black_money, white_money):
    print("--- Accountant Report ---")
    print(f"Total: {all_money} | Black: {black_money} | White: {white_money}")

if __name__ == "__main__":
    print("Running internal test...")
    m = int(input("Enter total money: "))
    b = int(input("Enter black money: "))
    w = int(input("Enter white money: "))
    tax_information(m, b, w)
else:
    print("my_module has been imported successfully!")