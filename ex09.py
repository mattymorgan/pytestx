#!/usr/bin/python

'''
9. Find all of the crypto map entries 
that are using PFS group2
'''

from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse("cisco_ipsec.txt")

# Find all crypto map entries using PFS group2 under crypto map

g2 = cfg.find_objects_w_child(parentspec=r"^crypto map", childspec=r"group2") 

print "The following entries are using PFS Group 2:"
for each in g2:
    print each.text
