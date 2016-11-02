#!/usr/bin/env python

import pysnmp
from snmp_helper import snmp_get_oid, snmp_extract

C_STRING = 'galileo'
IP = '192.168.56.100'
PORT = '161'

a_device = (IP, C_STRING, PORT)

# Two OIDs for testing
desc_oid = '1.3.6.1.2.1.1.1.0'
host_oid = '1.3.6.1.2.1.1.5.0'

# Current uptime
sysUptime = '1.3.6.1.2.1.1.3.0'

OID = desc_oid

snmp_data = snmp_get_oid(a_device, oid=OID)
output = snmp_extract(snmp_data)

print output
