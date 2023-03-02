import requests
import json

username= "surkuruv"
password="Suri@2321"
print("                Signing in / obtaining access token      ")

url = 'https://corona.cisco.com/users/sign_in.json'

res = requests.post(url, json={
   "user": {
      "username": username,
      "password": password
   }
})
res_json = res.json()
print(res_json)
