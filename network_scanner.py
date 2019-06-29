#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest = "target",help ="Target IP/ I{ range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answerd_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose=False)[0]

    clients_list = []
    for element in answerd_list:
        client_dict  ={"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict) 
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n---------------------")
    for target in result_list:
        print(target["ip"] + "\t\t" + target["mac"])

options = get_arguments()
scan_results = scan(options.target)
print_result(scan_results)