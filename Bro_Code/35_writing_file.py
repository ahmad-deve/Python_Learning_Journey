# txt_data = "I love my pakistan."
file_path = "35_love_from_ahmad.txt"
with open (file_path,"a") as file:
    file.write("i also love computer.")
    # print(file.read())
    # print()

# advance practice
import os
file_dir = "35_love_from_ahmad.txt"
if os.path.exists:
    print("this file is exists.")
    with open(file_dir,"r") as file:
        print(file.read())
else:
    print("the file is not exists.")