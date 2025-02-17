import subprocess

def ip_scan(target):
    print("\n[+] Starting IP scan...")
    
    # Using nmap for scanning (you can use other tools like masscan)
    try:
        result = subprocess.run(
            f"nmap -sV -oG - {target}",
            shell=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"[!] Error during IP scan: {e}")

if __name__ == "__main__":
    target = input("Enter target IP or range: ")
    ip_scan(target)