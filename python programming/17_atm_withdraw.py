try: 
    user_ammount = int(input("Enter the withdraw ammount: "))
    user_blance = 500

    if user_ammount <= user_blance:
        print(f"your full balance is {user_blance} and after you withdraw your balance is {user_blance-user_ammount}.")
    else:
        print("you enter the unvaild funds!")
except:
    print("only add the numerical number.")