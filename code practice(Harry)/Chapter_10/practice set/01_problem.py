g = open("file.txt")
content = g.read()
if ("Ahmad" in content):
    print("this is about the ahmad.")
else:
    print("This is not about the ahmad.")
g.close()