#!/usr/bin/env python
import scapy.all as scapy
import argparse
from scapy_http import http as http

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="Interface")
    options = parser.parse_args()
    return options


def process_sniffed_packet(packet):
    
    if(packet.haslayer(http.HTTPRequest)):
        print(packet)
        

def sniff(interface):
    scapy.sniff(iface=interface,prn = process_sniffed_packet)


#  Parse the arguments
options = parse_arguments()
interface_specified = options.interface

#Sniff the trafic
sniff(interface_specified)