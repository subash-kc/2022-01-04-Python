#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line

        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address

        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:
        print('Could not collect adapter information') # Print an error message

def extract_ip(ifname):

    print(( netifaces.ifaddresses(ifname)[netifaces.AF_LINK]



