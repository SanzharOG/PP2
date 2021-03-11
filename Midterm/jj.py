import json
a=input()
data=json.loads(a)
min=10000000000
for i in data["Subscriptions"]:
    if int(i["price"])*(1-(int(i["discount"])/100))<min:
        min=round(int(i["price"])*(1-(int(i["discount"])/100)))
        x=i
month=x["name"]
print("Name:", month)
print("Price:", min)
