#!/usr/bin/env python

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit('Error: Connection attempt timed-out')
 
def login(remote_conn, username, password):
    output = remote_conn.read_until('sername:', TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until('assword:', TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output
 
def send_command(remote_conn, command):
    # Strip off trailing whitespace with rstrip
    command = command.rstrip()
    remote_conn.write(command + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()
      
def main():
    ip_addr = '192.168.56.100'
    username = 'admin'
    password = 'password'
    
    remote_conn = telnet_connect(ip_addr)
    login(remote_conn, username, password)
    
    output = send_command(remote_conn, 'ter len 0')
    output = send_command(remote_conn, 'show ip int br')
    print(output)

    remote_conn.close()


if __name__ == '__main__':
    main()
