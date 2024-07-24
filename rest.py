# The following example is a request using the requests module in Python

# 1. First we will import the necessary libraries. Requests is used to perform CRUD actions on the API. JSON is used to
#    parse the data into a familiar data serialization language (Javascript Object Notation)

import requests
import json

# 2. Using the requests library that is now imported, we can perform a read operation (HTTP GET) and store the contents
#   of the returned data in a variable.

data = requests.get('https://api.restful-api.dev/objects').json()

print (data)
