import socket

def port_scan(target, ports=None):
    print("\n[+] Starting port scan...")
    
    if not ports:
        ports = range(1, 1000)  # Common ports
    
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
        except Exception as e:
            pass
    
    print("\nScan completed.")

if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = input("Enter ports to scan (comma-separated) or leave blank for common ports: ").split(',')
    
    if ports:
        ports = [int(p.strip()) for p in ports]
    else:
        ports = None
    
    port_scan(target, ports)