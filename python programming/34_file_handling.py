import json
data = {"Gander":"ali", "position": "intership","spending":10000}
with open("data.json","w") as file:
    json.dump(data,file)
with open("data.json","r") as file:
    content =   json.load(file)
    print(f"Content: {content}")