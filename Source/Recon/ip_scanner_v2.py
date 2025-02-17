import socket
import subprocess
import sys

def resolve_target(target):
    """Resolve a target name (domain or IP) to one or more IPs."""
    try:
        # Check if the target is an IPv4 address
        if socket.is_ipv4_address(target):
            return [target]
        # Try to resolve the domain to an IP
        ip = socket.gethostbyname(target)
        return [ip]
    except socket.gaierror as e:
        print(f"Error resolving target: {e}")
        return []

def scan_target(ip):
    """Scan a single IP using nmap."""
    try:
        # Run nmap command and capture output
        result = subprocess.run(
            f"nmap -sV -p- {ip}", 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            text=True,
            check=True
        )
        print(f"\nScan completed for IP: {ip}")
        print("------------------------------------------------------------")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error scanning IP {ip}: {e}")

def main():
    print("\nReconnaissance Scanner")
    print("----------------------")
    
    # Get target input
    target = input("Enter target (IP or domain): ")
    
    # Resolve the target to IPs
    ips = resolve_target(target)
    
    if not ips:
        print("Invalid target. Please enter a valid IP or domain.")
        return
    
    # Scan each resolved IP
    for ip in ips:
        scan_target(ip)

if __name__ == "__main__":
    main()