##Network Scanner (Gets IP and MAC addressees of devices in a network)

from scapy.all import ARP, Ether, srp
#make an ARP (address resolution protocol request and send to all devices in your network)
targetIP = "127.0.0.1"
#anyone with the target IP will reply back and send their MAC address and IP back.
#we can now assign this MAC to ourselves use it for spoofing

#make arp
arp = ARP(pdst = targetIP)

#ff is for broadcast
ether = Ether(dst = "ff:ff:ff:ff:ff:ff")

#stack them
packet = ether/arp

# [0]: Extracts the first element of the returned list, which contains the sent and received packets.
result = srp(packet, timeout = 3, verbose = 0)[0]
print(result)
clients = []

for sent, recieved in result:
  clients = clients.append({'ip': recieved.psrc, 'MAC': recieved.hwsrc})

#print
print("Available devices in the network:")
print("IP" + " "+"MAC")
for client in clients:
    print(client['ip'], client['mac'])
