with open("About_Ahmad.txt","r+") as file:
    file.write("Ahmad is the programmar. He is currently learning the python.")
    print("Writing successfully!")
    content = file.read()
    print(f"The content file: {content}")
file.close()

# with open("About_Ahmad.txt","w") as file:
#     file.write("This is the about ahmad:!")
#     print('write successfully!')
# file.close()