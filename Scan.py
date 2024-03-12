#!/usr/bin/python3

import os
import nmap

print("[Info] Herramienta para escanear los puertos abiertos en una dirección IP")
print("  ||   Escrito en Python y utiliza Nmap")
print("  || Escrita por gustavo Lobato\n")

ip=input("[+] IP Objetivo ==> ")
nm = nmap.PortScanner()
puertos_abiertos="-p "
# Use proxychains to run nmap scan through Tor
os.system('proxychains nmap -sT -n -Pn -T4 -f --script -all -p ' + ip)
count=0
#print (results)
print("\nHost : %s" % ip)
print("State : %s" % nm[ip].state())
for proto in nm[ip].all_protocols():
    print("Protocol : %s" % proto)
    print()
    lport = nm[ip][proto].keys()
    sorted(lport)
    for port in lport:
        print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
        if count==0:
            puertos_abiertos=puertos_abiertos+str(port)
