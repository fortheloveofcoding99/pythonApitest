import requests
import json
import jsonpath
import pytest
# Api url
url = "https://reqres.in/api/users"

def test_create_new_user():
    # read input json file
    file = open('C:\\Users\\befor\\OneDrive\\Desktop\\apicreateuser.json', 'r')
    json_input = file.read()
    # parsing the file through json.loads since it is in a string format
    request_json = json.loads(json_input)
    print(request_json)
    # Make post request
    response = requests.post(url, request_json)
    print(response.content)
    # validating response code
    assert response.status_code == 201
    # fetch response to json format
    json_response = json.loads(response.text)
    # pick id from the json response
    id = jsonpath.jsonpath(json_response, 'id')
    print(id[0])

def test_create_another_user():
    # read input json file
    file = open('C:\\Users\\befor\\OneDrive\\Desktop\\apicreateuser.json', 'r')
    json_input = file.read()
    # parsing the file through json.loads since it is in a string format
    request_json = json.loads(json_input)
    print(request_json)
    # Make post request
    response = requests.post(url, request_json)
    print(response.content)
    # validating response code
    assert response.status_code == 200
    # fetch response to json format
    json_response = json.loads(response.text)
    # pick id from the json response
    id = jsonpath.jsonpath(json_response, 'id')
    print(id[0])


