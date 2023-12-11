## README.md

This repository contains a Python script that utilizes Scapy to identify and list active devices on your network.

### What it does

* Scans the local network using the Address Resolution Protocol (ARP).
* Retrieves the IP and MAC addresses of all connected devices.
* Displays the information in a clear and concise table format.

### Requirements

* Python 3.x
* Scapy library (install with `pip install scapy`)

### Usage

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the following command:

```
python network_scanner.py
```

4. The script will scan the network and display the list of discovered devices.

### Output

The script will print a table containing the following information for each device:

* IP Address
* MAC Address

### Example

```
Available devices in the network:

IP             MAC
---------------------
192.168.1.10  00:AA:BB:CC:DD:EE
192.168.1.20  FF:FF:FF:FF:FF:FF
192.168.1.30  11:22:33:44:55:66
```

### Contributing

We welcome contributions to improve this script. If you have any suggestions or bug fixes, please create a pull request.

### Disclaimer

Please use this script responsibly and only within your authorized network. Do not use it to scan networks without permission.
