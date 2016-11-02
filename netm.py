#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler, FileTransfer

def main():
    net_device = { 'device_type': 'cisco_ios',
                    'ip': '192.168.56.105',
                    'username': 'admin',
                    'password': 'password',
    }

    print("\nLogging in to Router")
    ssh_conn = ConnectHandler(**net_device)
    print()

    # GET OPERATION
    source_file = 'config_backup.txt'
    dest_file = 'config_backup.txt'
    dest_file_system = 'flash:'
    with FileTransfer(ssh_conn, 
                      source_file=source_file, 
                      dest_file=dest_file,
                      file_system=dest_file_system, 
                      direction='get') as scp_transfer:
        scp_transfer.get_file()
        print("File transfer completed\n\n")

if __name__ == "__main__":
    main()
