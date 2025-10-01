import json

with open("slicing.json", "r") as f:
    data = json.load(f)

for item in data:   # data is a LIST, loop through it
    print("Username:", item["name"])
    print("Domain:", item["email"])
    print("-" * 20)
