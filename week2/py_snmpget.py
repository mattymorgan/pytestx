from snmp_helper import snmp_get_oid,snmp_extract

import pickle

# Basic setup for snmp target
COMMUNITY_STRING = 'galileo'
R1_SNMP_PORT= 7961
R2_SNMP_PORT= 8061
IP = '50.242.94.227'

# Two OIDs for testing
desc_oid = '1.3.6.1.2.1.1.1.0'
host_oid = '1.3.6.1.2.1.1.5.0'

# Current uptime
sysUptime = '1.3.6.1.2.1.1.3.0'

# Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'

# Uptime when running config last saved (note any 'write' constitutes a save)
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'

# Uptime when startup config last saved
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

# Tuples for each device
r1 = (IP, COMMUNITY_STRING, R1_SNMP_PORT)
r2 = (IP, COMMUNITY_STRING, R2_SNMP_PORT)

# List of devices
device_list = [r1, r2]

# List of OIDs to lookup
oid_list = [host_oid, desc_oid]

# List of config OIDs to test last changed/save timestamp values
config_oid_list = [sysUptime, ccmHistoryRunningLastChanged, ccmHistoryRunningLastSaved, ccmHistoryStartupLastChanged]

# List to store OID values
returned_data = []

# Secondary list for OID timestamp values
config_timestamp = []


# Lookup function to return string value
def lookup(my_device, my_oid):
    snmp_data = snmp_get_oid(device, oid=my_oid)
    output = snmp_extract(snmp_data)
    return output

# append values for each device OID
for device in device_list:
    for oid in oid_list:
        returned_data.append(lookup(device, oid))
    
    for oid in config_oid_list:
        config_timestamp.append(lookup(device, oid))
        
for item in returned_data:
    print item + "\n" 

for item in config_timestamp:
    #print item 
    pass

# check the timestamp values 
# this only works with the last item in the list    
def check_save(data):
    uptime = int(data[0])
    running_last_changed = int(data[1]) 
    running_last_saved = int(data[2])
    startup_last_changed = int(data[3])

    # try to read file containing previous uptime value
    # not really sure how this affects the state of changed/saved values
    try:
        f = open("temp.pkl", "rb")
        prev_uptime = pickle.load(f)
        f.close()
        if prev_uptime > uptime:
            print "Device has been rebooted since last check"
    
    except:
        pass
    
    # try to write the current uptime value
    try:
        f = open("temp.pkl", "wb")
        pickle.dump(uptime, f)  
        f.close()
        
    except:
        pass
     
    print "Current Uptime: " + str(uptime)
    print "Uptime when running config last changed: " + str(running_last_changed)
    print "Uptime when running config last saved:   " + str(running_last_saved)
    print "Uptime when startup config last changed: " + str(startup_last_changed)
    
    # if running_last_changed > running_last_saved means we 
    # didn't save the config to NVRAM
    
    # if running_last_changed < running_last_saved but
    # running_last_saved not equal to statup_last_changed, means we
    # didn't save the config to NVRAM
    
    if running_last_changed < running_last_saved:
        if running_last_saved != startup_last_changed:
            print "Warning: Configuration not saved to NVRAM"

    else:
         print "Warning: Configuration not saved to NVRAM"

# this only works with the last item in the list  
check_save(config_timestamp)
