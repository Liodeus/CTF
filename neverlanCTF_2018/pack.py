#!/usr/bin/python

from scapy.all import *
import yenc


pkts = rdpcap("./private.pcap")
fichier = open("./file", "w")

for i in range(0, len(pkts)):
    fichier.write(pkts[i].load)
    print yenc.decode("./file", "./resultat")
