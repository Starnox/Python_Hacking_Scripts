#!/usr/bin/env python
import scapy.all as scapy
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="Interface")
    options = parser.parse_args()
    return options


def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn = lambda x: x.summary())


#Parse the arguments
options = parse_arguments()
interface_specified = options.interface

#Sniff the trafic
sniff(interface_specified)