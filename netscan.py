import socket
import os
from scapy.all import *

# Scan open ports
def port_scanner(ip, ports):
    print(f"\nScanning ports on {ip}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for faster scanning
            if sock.connect_ex((ip, port)) == 0:
                print(f"Port {port} is open")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# Ping a device
def ping_device(ip):
    print(f"\nPinging {ip}...")
    os.system(f"ping -c 4 {ip}")

# Discover devices
def arp_scan():
    print("\nPerforming ARP scan...")
    try:
        answered, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.0/24"), timeout=2, verbose=0)
        devices = [p[ARP].psrc for p in answered]
        print("Discovered devices:")
        for device in devices:
            print(device)
    except Exception as e:
        print(f"Error performing ARP scan: {e}")

# Trace route
def trace_route(ip):
    print(f"\nTracing route to {ip}...")
    os.system(f"traceroute {ip}")

# Host information
def host_info(domain):
    print(f"\nFetching host information for {domain}...")
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP address of {domain} is {ip}")
    except Exception as e:
        print(f"Error fetching host information: {e}")

# Main Program
def main():
    while True:
        print("\nNetwork Utility Menu:")
        print("1. Port Scanner")
        print("2. Ping a Device")
        print("3. Discover Devices (ARP Scan)")
        print("4. Trace Route")
        print("5. Host Information")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            ip = input("Enter the target IP: ")
            ports = input("Enter comma-separated port numbers (e.g., 22,80,443): ")
            ports = [int(p.strip()) for p in ports.split(",")]
            port_scanner(ip, ports)
        elif choice == "2":
            ip = input("Enter the target IP: ")
            ping_device(ip)
        elif choice == "3":
            arp_scan()
        elif choice == "4":
            ip = input("Enter the target IP or domain: ")
            trace_route(ip)
        elif choice == "5":
            domain = input("Enter the domain name: ")
            host_info(domain)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
