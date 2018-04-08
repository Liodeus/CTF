from scapy.all import *

r = rdpcap("neverlan.pcapng")

data = ''

for i in range(0, len(r)):
    if ICMP in r[i]:
        if r[i][ICMP].type == 8:
            data += str(r[i][ICMP].code)

flag = ''
for x in range(0, len(data), 8):
    flag += chr(int(data[x:x+8], 2))

print(flag)
