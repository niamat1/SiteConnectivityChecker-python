#site connectivith checker
import requests
address = input("type your website address = ")
code = requests.get(address).status_code

if code == 200:
    print("online")
else:
    print("offline")