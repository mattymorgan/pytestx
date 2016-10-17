#!/usr/bin/python
'''
6. Write a Python program that creates a list. 
One of the elements of the list should be a dictionary
with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file
should be in the expanded form.
'''


import yaml
import json

# Create a list, with one element as a dictionary
my_list = ["foo", "bar", 1, 2, 3, "abc", "def"] 
my_list.append({})
my_list[-1]['ip addr'] = '1.1.1.1'
my_list[-1]['atrribs'] = range(5)

print my_list

# Write the file in YAML format
with open("yaml_file.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

# Write the file in JSON format
with open("json_file.json", "w") as f:
    json.dump(my_list, f)
