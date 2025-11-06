import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

user_details = response.json()
 
for user in user_details:
  print(user["user"]["id"])