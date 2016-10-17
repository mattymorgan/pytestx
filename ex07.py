#!/usr/bin/python

'''
7. Write a Python program that reads both the 
YAML file and the JSON file created in 
exercise6 and pretty prints the data 
structure that is returned.
'''

import yaml
import json

from pprint import pprint as pp

# Read the file in YAML format and assign to a new_list
with open("yaml_file.yml") as f:
    yaml_list = yaml.load(f)

print("The YAML data:")
pp(yaml_list)

# Read the file in JSON format and assign to a new list
with open("json_file.json") as f:
    json_list = json.load(f)

print("The JSON data:")
pp(json_list)


