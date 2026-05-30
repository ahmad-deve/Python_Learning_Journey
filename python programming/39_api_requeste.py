import requests
url = "https://theahmad.site/blog/"
response = requests.get(url) 
print(f"Status code: {response.status_code}")
print("content: ",response.text)
with open("index.html","w") as f:
    f.write(response.text)