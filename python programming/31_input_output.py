# with open("sample.txt","w") as file:
#     file.write("This is the sample file. only creating for the test")
# print("the txt writien in file successfully.")

# with open("sample.txt","a") as file:
#     file.write("\nnow i add the more text")
# print("the append is successfully!")

with open("sample.txt","r+") as file:
    content = file.read()
    print(f"Current Content is:  {content}.")
    file.write("\n This is an adding the line using the r+ mode.")
    print("writing successfully!")
file.close()