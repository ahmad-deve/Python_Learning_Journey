import os
file_path = "33_test.txt"
if os.path.exists(file_path):
    print(f"The location of {file_path} is exists.")
else:
    print("The path is not exists. ")