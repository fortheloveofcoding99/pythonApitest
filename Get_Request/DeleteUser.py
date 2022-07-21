import requests

# API URL
url = "https://reqres.in/api/users/39"

Delete_response = requests.delete(url)

#Fetch Response Code

print (Delete_response.status_code)

assert Delete_response.status_code == 204