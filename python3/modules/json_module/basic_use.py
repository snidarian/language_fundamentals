#!/usr/bin/python3


import json


# json string
girlfriends_string = '''
{
    "girlfriends": [
        {
            "name": "Betty loo who",
            "phone": "594-333-2093",
            "hair": "blonde",
            "temperment": ["jovial", "silly"]
        },
        {
            "name": "Cindy loo who",
            "phone": "394-428-4892",
            "hair": "brunette",
            "temperment": ["somber", "grave"]
        },
        {
            "name": "Karen roo due",
            "phone": "492-283-2939",
            "hair": "redhead",
            "temperment": ["playful", "thoughtful"]
        }
    ]
}

'''

# .loads() method creates python object from json string
data = json.loads(girlfriends_string)
print(data)


# we can itterate through the list of python objects now.
for girlfriend in data['girlfriends']:
    print(girlfriend['name'])
    print(girlfriend['hair'])
    del girlfriend['phone']



# Turn python object into a json string
# indent sets number of indents for each level of data.
# sort_keys - when True sorts keys by alphabetical order
new_json_object = json.dumps(data, indent=1, sort_keys=True)

print(new_json_object)

# Creates a json file with the data in it
# The file should appear in the same directory as this file
with open('json_example_file.json', 'w') as f:
    json.dump(new_json_object, f, indent=2)













