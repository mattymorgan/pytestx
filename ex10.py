#!/usr/bin/python

'''
9. Find all of the crypto map entries 
that are using PFS group2
'''

from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse("cisco_ipsec.txt")

# Find all crypto map entries not using AES transform-set under crypto map

no_aes = cfg.find_objects_wo_child(parentspec=r"^crypto map", childspec=r"AES") 

print "The following entries are not using AES:"
for each in no_aes:
    print each.text
    for line in each.parent.all_children:
        print line.text
    print
