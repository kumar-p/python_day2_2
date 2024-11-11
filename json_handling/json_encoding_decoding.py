import json

file_path = 'data/avengers.json'

with open(file_path, 'r') as file:
    json_string = file.read()

print(json_string)

# read json string and convert it to python object
json_data = json.loads(json_string)

print(type(json_data))
print(type(json_data[0]))
print(json_data[0]['name'])

# read json from file and convert it to python object
with open(file_path, 'r') as file:
    data = json.load(file)

print(type(data))
print(type(data[0]))
print(data[0]['name'])

# convert python object to json string
iron_man = {
    "name": "Iron Man",
    "real_name": "Tony Stark",
    "abilities": ["Genius-level intellect", "Proficient scientist and engineer", "Powered armor suit"]
}
pretty_json = json.dumps(json_data, indent=4)
print(pretty_json)

# convert python object to json string and write to file
with open('data/iron_man.json', 'w') as file:
    json.dump(iron_man, file, indent=4)
