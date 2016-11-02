#!/usr/bin/env python
'''
a. Make sure that you have PySNMP and Paramiko installed in the 
lab (i.e. enter the Python shell and test 'import pysnmp', and
'import paramiko').

b. Determine which version of PySNMP and Paramiko are installed.  
dir(pysnmp) and dir(paramiko) should be helpful here.

'''
import pysnmp
import paramiko

pysnmp_ver = pysnmp.__version__
paramiko_ver =  paramiko.__version__

def print_versions():
    version_string = (
            "PySNMP is version: {}, Paramiko is version: {} ".format(
                pysnmp_ver, paramiko_ver))

    return version_string

print(print_versions())
