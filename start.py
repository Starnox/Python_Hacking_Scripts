#!/usr/bin/env python3

import subprocess as sb
import optparse

parser = optparse.OptionParser()

def change_mac():
    parser.add_option("-i","--interface", dest="interface", help= "Interface to change its MAC ADRRES")
    parser.add_option("-m","--mac", dest="new_mac", help= "New Mac Address")
    (options, arguments) =  parser.parse_args()
    interface = options.interface
    new_mac = options.new_mac

#sb.call(["ifconfig",interface,"down"])
#sb.call(["ifconfig",interface,"hw",new_mac])
#sb.call(["ifconfig",interface,"up"])

