from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

broadcast = "ff:ff:ff:ff:ff:ff"
ip_range = "192.168.1.1/24"  # Fixed the IP range format (added .1)

my_arp_layer = ARP(pdst=ip_range)
ether_layer = Ether(dst=broadcast)
# Send and receive packets
packet = ether_layer / my_arp_layer

ans, unans = srp(packet, iface="eth0", timeout=2)

for snd, rcv in ans:
    print(f"IP: {rcv.psrc} MAC: {rcv.hwsrc}")
    # print(f"IP: {rcv.psrc} MAC: {rcv.hwsrc} Vendor: {get_mac_vendor(rcv.hwsrc)}")