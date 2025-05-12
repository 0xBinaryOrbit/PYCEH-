import subprocess


if __name__ == "__main__":
    interface = "eth0"
    new_mac = "00:11:22:33:44:55"

    print(f"Shutting down the network {interface.upper()} interface...")
    subprocess.run(["ifconfig",interface, "down"])
    print(f"Changing MAC address of {interface.upper()} to {new_mac}...")
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    print(f"Bringing up the network {interface.upper()} interface...")