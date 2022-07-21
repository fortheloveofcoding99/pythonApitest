import requests
import json
import jsonpath
# Api url

url = "https://reqres.in/api/users/332"

# read input json file

file = open('C:\\Users\\befor\\OneDrive\\Desktop\\apicreateuser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

#Make put request with json input body

response = requests.put(url,request_json)
print(response.content)

# validating response code
assert response.status_code == 200

# parsing the response content

response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,"updatedAt")
print (updated_li[0])