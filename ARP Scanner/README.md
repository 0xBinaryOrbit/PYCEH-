# arp-scanner-py

A lightweight Python script using Scapy to perform ARP scans across a local network subnet. This tool helps in identifying live hosts and their MAC addresses within a given IP range.

---

## ⚙️ Features

- Scans a specified IP range using ARP requests
- Prints the IP and MAC address of each responsive device
- Uses Scapy for low-level packet crafting
- Useful for network inventory, penetration testing, or troubleshooting

---

## 📦 Requirements

- Python 3.x
- Root privileges (required for sending ARP packets)
- Scapy Python library

Install Scapy using pip:
```bash
pip install scapy
```

---

## 🛠️ Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/arp-scanner-py.git
cd arp-scanner-py
```

2. Run the script (make sure to use `sudo` or run as root):
```bash
sudo python3 arp_scanner.py
```

3. Default settings (can be modified inside the script):
```python
ip_range = "192.168.1.0/24"
iface = "eth0"
```

---

## 📌 Example Output

```text
IP: 192.168.1.1 MAC: aa:bb:cc:dd:ee:ff
IP: 192.168.1.10 MAC: 11:22:33:44:55:66
```

---

## 🚨 Disclaimer

This tool is intended for ethical and legal use only. Unauthorized scanning of networks you do not own or have explicit permission to test is illegal and unethical.

---



## 🔗 Author
**Faisal khan**  
GitHub: [Faisal Khan](https://github.com/mrfaisal607)