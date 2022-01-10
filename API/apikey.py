# way to interact one computer to another

# api deals with the aw data

import requests

url = "https://google.com"

r = requests.get(url)

print(r)

# print(r.text)

# print(r.content)

example_data = {"people"}

print(r.json())
