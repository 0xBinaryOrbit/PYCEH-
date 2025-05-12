# mac-changer-py

A simple Python tool to change the MAC (Media Access Control) address of a network interface on Linux systems. This utility can be used for privacy testing, network forensics, and administrative tasks where MAC address spoofing is required.

---

## ⚙️ Features

- Change the MAC address of any specified interface (e.g., eth0, wlan0)
- Easy-to-use script using Python's `subprocess` module
- Minimal and clean design
- Fully customizable for different interfaces and MAC addresses

---

## 📦 Requirements

- Python 3.x
- Linux operating system
- Root privileges (required to change MAC addresses)
- `ifconfig` command (comes with `net-tools` package)

To install `ifconfig` if missing:
```bash
sudo apt install net-tools
```

---

## 🛠️ Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/mac-changer-py.git
cd mac-changer-py
```

2. Open and edit the script to specify your desired interface and MAC address:
```python
interface = "eth0"
new_mac = "00:11:22:33:44:55"
```

3. Run the script with root privileges:
```bash
sudo python3 mac_changer.py
```

---

## 📌 Example Output

```text
Shutting down the network ETH0 interface...
Changing MAC address of ETH0 to 00:11:22:33:44:55...
Bringing up the network ETH0 interface...
```

---

## 🚨 Disclaimer

This tool is intended for educational and ethical use only. Unauthorized MAC address spoofing on networks you don't own or have permission to test is illegal and unethical. Always ensure you have the right to perform any network modifications.

---


## 🤝 Contributing

Pull requests and suggestions are welcome! Feel free to fork the repository and submit changes.

---

## 🔗 Author

**Faisal khan**  
GitHub: [Faisal Khan](https://github.com/mrfaisal607)
