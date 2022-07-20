import requests
import json
import jsonpath
# Api url

url = "https://reqres.in/api/users?page=2"

# send get request and display the content of the response

response = requests.get(url)

#parsing the response in the form of JSON

json_response = json.loads(response.text)
print(json_response)

#fetch value using Json Path
totalFields = jsonpath.jsonpath(json_response,'total') #jsonPath always returns a list
assert totalFields[0] == 12