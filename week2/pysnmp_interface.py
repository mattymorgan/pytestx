#!/usr/bin/env python

from pysnmp.entity.rfc3413.oneliner import cmdgen
import sys
import re

device = "192.168.56.198"
community = "galileo"

def interface_list(x):
    int_name  = []
    int_oid = []
    try:
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
            cmdgen.CommunityData(community),
            cmdgen.UdpTransportTarget((x, 161)),
            '1.3.6.1.2.1.2.2.1.2',
        )
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                oid_raw = name.prettyPrint()
                oid = re.search(r'1.3.6.1.2.1.2.2.1.2.(\d{0,5})', oid_raw)
                oid = oid.group(1)
                int_oid.append(oid)
                int_name.append(val.prettyPrint())
        return int_oid, int_name
    except:
        return None

'''
print interface_list(device)
(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '19', '20'], ['FastEthernet0/0', 'FastEthernet1/0', 'FastEthernet1/1', 'FastEthernet1/2', 'FastEthernet1/3', 'FastEthernet1/4', 'FastEthernet1/5', 'FastEthernet1/6', 'FastEthernet1/7', 'FastEthernet1/8', 'FastEthernet1/9', 'FastEthernet1/10', 'FastEthernet1/11', 'FastEthernet1/12', 'FastEthernet1/13', 'FastEthernet1/14', 'FastEthernet1/15', 'Null0', 'Vlan1'])
'''        

def interface_admin(x):
    int_admin  = []
    admin = ''
    try:
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
            cmdgen.CommunityData(community),
            cmdgen.UdpTransportTarget((x, 161)),
            '1.3.6.1.2.1.2.2.1.7',
        )
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                admin_raw = val.prettyPrint()
                if '1' in admin_raw:
                    admin = 'UP'
                elif '2' in admin_raw:
                    admin = 'DOWN'
                elif '3' in admin_raw:
                    admin = 'TESTING'
                int_admin.append(admin)
        return int_admin
    except:
        return None

'''    
print interface_admin(device)
['UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'DOWN']
'''

def interface_oper(x):
    int_oper  = []
    oper = ''
    try:
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
            cmdgen.CommunityData(community),
            cmdgen.UdpTransportTarget((x, 161)),
            '1.3.6.1.2.1.2.2.1.8',
        )
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                oper_raw = val.prettyPrint()
                if '1' in oper_raw:
                    oper = 'UP'
                elif '2' in oper_raw:
                    oper = 'DOWN'
                elif '3' in oper_raw:
                    oper = 'TESTING'
                elif '4' in oper_raw:
                    oper = 'UNKNOWN'
                elif '5' in oper_raw:
                    oper = 'DORMANT'
                elif '6' in oper_raw:
                    oper = 'NOT-PRESENT'
                elif '7' in oper_raw:
                    oper = 'LOWER-LAYER-DOWN'
                int_oper.append(oper)
        return int_oper
    except:
        return None

'''    
print interface_oper(device)
['UP', 'UP', 'UP', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'UP', 'DOWN']
'''

def interface_time(x):
    int_time  = []
    try:
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
            cmdgen.CommunityData(community),
            cmdgen.UdpTransportTarget((x, 161)),
            '1.3.6.1.2.1.2.2.1.9',
        )
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                int_time.append(val.prettyPrint())
                
        return int_time
    except:
        return None

'''    
print interface_time(device)
['2213', '601', '600', '600', '599', '598', '598', '597', '596', '595', '594', '594', '593', '592', '592', '591', '590', '0', '582']
'''

from prettytable import PrettyTable

print "Checking for interfaces..."
oid, name = interface_list(device)

if name:
    admin = interface_admin(device)
    oper = interface_oper(device)
    time = interface_time(device)
    print "Done"
    table = PrettyTable(["OID Value","Interface Name","Admin Status","Operational", "Time"])
    for i in range(len(name)):
        table.add_row(["1.3.6.1.2.1.2.2.1.2."+oid[i],name[i],admin[i],oper[i],time[i]])
    print "\n\n"
    print table

'''    
Done



+------------------------+------------------+--------------+-------------+-------+
|       OID Value        |  Interface Name  | Admin Status | Operational |  Time |
+------------------------+------------------+--------------+-------------+-------+
| 1.3.6.1.2.1.2.2.1.2.1  | FastEthernet0/0  |      UP      |      UP     |  2213 |
| 1.3.6.1.2.1.2.2.1.2.2  | FastEthernet1/0  |      UP      |      UP     | 86406 |
| 1.3.6.1.2.1.2.2.1.2.3  | FastEthernet1/1  |      UP      |      UP     |  600  |
| 1.3.6.1.2.1.2.2.1.2.4  | FastEthernet1/2  |      UP      |     DOWN    |  600  |
| 1.3.6.1.2.1.2.2.1.2.5  | FastEthernet1/3  |      UP      |     DOWN    |  599  |
| 1.3.6.1.2.1.2.2.1.2.6  | FastEthernet1/4  |      UP      |     DOWN    |  598  |
| 1.3.6.1.2.1.2.2.1.2.7  | FastEthernet1/5  |      UP      |     DOWN    |  598  |
| 1.3.6.1.2.1.2.2.1.2.8  | FastEthernet1/6  |      UP      |     DOWN    |  597  |
| 1.3.6.1.2.1.2.2.1.2.9  | FastEthernet1/7  |      UP      |     DOWN    |  596  |
| 1.3.6.1.2.1.2.2.1.2.10 | FastEthernet1/8  |      UP      |     DOWN    |  595  |
| 1.3.6.1.2.1.2.2.1.2.11 | FastEthernet1/9  |      UP      |     DOWN    |  594  |
| 1.3.6.1.2.1.2.2.1.2.12 | FastEthernet1/10 |      UP      |     DOWN    |  594  |
| 1.3.6.1.2.1.2.2.1.2.13 | FastEthernet1/11 |      UP      |     DOWN    |  593  |
| 1.3.6.1.2.1.2.2.1.2.14 | FastEthernet1/12 |      UP      |     DOWN    |  592  |
| 1.3.6.1.2.1.2.2.1.2.15 | FastEthernet1/13 |      UP      |     DOWN    |  592  |
| 1.3.6.1.2.1.2.2.1.2.16 | FastEthernet1/14 |      UP      |     DOWN    |  591  |
| 1.3.6.1.2.1.2.2.1.2.17 | FastEthernet1/15 |      UP      |     DOWN    |  590  |
| 1.3.6.1.2.1.2.2.1.2.19 |      Null0       |      UP      |      UP     |   0   |
| 1.3.6.1.2.1.2.2.1.2.20 |      Vlan1       |     DOWN     |     DOWN    |  582  |
+------------------------+------------------+--------------+-------------+-------+
'''
