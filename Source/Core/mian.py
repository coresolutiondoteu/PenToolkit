from recon.ip_scanner import ip_scan
from recon.port_scanner import port_scan
from vulnerability_detection.http_vulns import http_cve_scan
from exploitation.http_exploits import exploit_http

def main():
    print("PenToolkit v0.1")
    while True:
        print("\nOptions:")
        print("1. IP and Network Reconnaissance")
        print("2. Port and Service Enumeration")
        print("3. Vulnerability Detection (HTTP)")
        print("4. Exploitation (HTTP)")
        print("5. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            ip_scan()
        elif choice == "2":
            port_scan()
        elif choice == "3":
            http_cve_scan()
        elif choice == "4":
            exploit_http()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()