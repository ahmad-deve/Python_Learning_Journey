defualt_mail = ["theahmadpro27@gmail.com"]
user_email = input("Enter you email: ")
if user_email in defualt_mail:
    print("Can proceed next!")
else:
    print("invalid mail")
user_passowrod = ("123456789")
user_input_password = input("Enter your password: ")
if user_input_password in user_passowrod:
    print("Now, you are log in")
    