#!/usr/bin/python

'''
8. Write a Python program using ciscoconfparse
that parses this config file. Note, this 
config file is not fully valid 
(i.e. parts of the configuration are missing). 
The script should find all of the crypto map 
entries in the file (lines that begin with 
'crypto map CRYPTO') and for each crypto map 
entry print out its children.
'''

from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse("cisco_ipsec.txt")

# Find all crypto map entries
crypto_maps = cfg.find_objects(r"^crypto map CRYPTO")

# For each crypto map (could be many)...
for entry in crypto_maps:
    # Print newline...
    print
    # Print entry header (map entry ref)...
    print entry.text	
    # Print all remaining info
    for child in entry.all_children:
        print child.text
