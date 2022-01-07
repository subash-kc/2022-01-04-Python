#!/usr/bin/env python3

"""
Only import the call and and check_output functions from teh subprocess module.


"""

from subprocess import call

call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")

#prompt the interface

interface = input("Enter an interface, like, ens3: ")
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])

