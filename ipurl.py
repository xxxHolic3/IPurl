#! /usr/bin/env python
from socket import *

print (" _____ _____            _ ")
print ("|_   _|  __ \          | |")
print ("  | | | |__) |   _ _ __| |")
print ("  | | |  ___/ | | | '__| |")
print (" _| |_| |   | |_| | |  | |")
print ("|_____|_|    \__,_|_|  |_|")
print ("[*] Version 1")
print ("[*] @Falcon")
print ("[*] This software is under GNU General Public License v3.0")                         
                          
host = input("\n[*] Target url : ")
getip = gethostbyname(host)
print ("[*] Target IP  :", getip)
print ("Hapyy Hunting !!! :D")
