# Json format data
# adding entire dictionary in single quotes called as json format
"""
import json

emp = '{"name": "RNS Tech", "age": 15, "salary": "2L"}'

data = json.loads(emp)

print(data["name"])
print(data["age"])
print(data["salary"])

#  https://jsonplaceholder.typicode.com/posts
# getting data from above URL
import requests, json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
# if we get 200 status that means we are able to connect url
# print(response.json())

data = response.json()

for row in data:
    print(row["userId"])

#All HTTP methods are supported. You can use http or https for your requests.

#GET	/posts
#GET	/posts/1
#GET	/posts/1/comments
#GET	/comments?postId=1
#POST	/posts
#PUT	/posts/1
#PATCH	/posts/1
#DELETE	/posts/1


# deleting data from URL
import requests, json

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print(response.json())


# putting data in to URL
import requests, json

inputdata = {
                "title": "Rnstech",
                "userId": 1,
                "body": "Example data"
            }
response = requests.post("https://jsonplaceholder.typicode.com/posts", data=inputdata)
print(response.status_code)
data = response.json()

print(data)


#CRUD operations
# creating, reading, updating and deleting
#openai api,
#rapidapi is third party for providing api services

import http.client, json

conn = http.client.HTTPSConnection("linkedin-data-api.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "a69df570e7msha237486d03213c4p141a9fjsna97f087d6fff",
    'x-rapidapi-host': "linkedin-data-api.p.rapidapi.com"
}

conn.request("GET", "/?username=gvenkat09", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

profile = json.loads(data)

print(profile["firstName"])
print(profile["lastName"])

"""


