# -- AUTHOR --
# Ryan Jahnke

# -- TITLE --
# rest.py

# -- SUMMARY --
# The following example is a GET request using the requests module in Python. This script summarizes in comments each
# section of code, and what is being accomplished. I'm using a public REST API in this example, found here:
# https://restful-api.dev/
# This script should show you:
# 1. How to perform a HTTP GET request to a REST API without any authentication
# 2. How to load this data into a variable, and print it in a human-readable format
# 3. How to loop through the objects in the returned data and print each
# 4. How to use for loops gather key-value pair information
# 5. When there are nested objects with key-value pairs, how to obtain those nested key-values
# Note that this example does not include any authentication -- this will be touched on in a separate script.


# -- CODE --
# 1. First we will import the necessary libraries. Requests is used to perform CRUD actions on the API. JSON is used to
#    parse the data into a familiar data serialization language (Javascript Object Notation)



import requests
import json



# 2. Using the requests library that is now imported, we can perform a read operation (HTTP GET) and store the contents
#   of the returned data in a variable. To "pretty-print" the JSON, we can use the json.dumps() function.



data = requests.get('https://api.restful-api.dev/objects').json()

readabledata = json.dumps(data, indent=4)

print (readabledata)
print ('\n\n\n')



# 3. Here we'll print out each object within the returned json data.



for objects in data:
    print (objects)
print('\n\n\n')



# 4. We can take it a step further and drill into each object and it's associated key-value pairs



for objects in data:
    for key in objects:
        if key == 'id':
            print ("Product ID # is: " + objects[key])
        if key == 'name':
            print ("Product name is: " + objects[key])



# 5. If we have a nested object, we can drill into this as well. Notice here I'm checking the parent object key name, and if it
#    matches the string 'data', and the associated value for the key 'data' is not data type 'None' (absense of value), I perform
#    another loop, printing the nested value for the nested key



        if (key == 'data') and (objects[key] != None):         
            for nestedkey in objects[key]:
                print (nestedkey + " is: " + str(objects[key][nestedkey]))
    print ('\n\n\n')



