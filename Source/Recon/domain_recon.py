import socket
import subprocess
import json
from datetime import datetime
from urllib.parse import urlparse

# Global variable to store the knowledge base
knowledge_base = {}

def gather_dns_information(domain):
    """Gather basic DNS information for a given domain."""
    try:
        # A record lookup
        a_records = socket.getaddrinfo(domain, 0)
        ip_addresses = [rhi.addrinfo.ip for rhi in a_records]
        
        # NS records
        ns_records = socket.getnameinfo(ipAddresses, 1)
        ns_hosts = [host for (_, host) in ns_records]
        
        return {
            'A Records': ip_addresses,
            'NS Records': ns_hosts
        }
    except Exception as e:
        print(f"Error gathering DNS information: {e}")
        return {}

def gather_whois_information(domain):
    """Gather WHOIS information for a given domain."""
    try:
        # Use whois command and parse output
        result = subprocess.run(
            f"whois {domain}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error gathering WHOIS information: {e}")
        return ""

def gather_mx_records(domain):
    """Gather MX records for a given domain."""
    try:
        # Use nslookup command to get MX records
        result = subprocess.run(
            f"nslookup -type=mx {domain}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=True
        )
        mx_records = []
        for line in result.stdout.split('\n'):
            if 'mail exchanger' in line.lower():
                parts = line.strip().split(' ')
                mailserver = parts[-1]
                mx_records.append(mailserver)
        return mx_records
    except subprocess.CalledProcessError as e:
        print(f"Error gathering MX records: {e}")
        return []

def gather_txt_records(domain):
    """Gather TXT records for a given domain."""
    try:
        # Use nslookup command to get TXT records
        result = subprocess.run(
            f"nslookup -type=txt {domain}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=True
        )
        txt_records = []
        for line in result.stdout.split('\n'):
            if 'text' in line.lower():
                parts = line.strip().split(' ')
                txt_record = ' '.join(parts[3:])
                txt_records.append(txt_record)
        return txt_records
    except subprocess.CalledProcessError as e:
        print(f"Error gathering TXT records: {e}")
        return []

def gather_spf_records(domain):
    """Gather SPF records for a given domain."""
    try:
        # Use nslookup command to get SPF records (type 'txt')
        txt_records = gather_txt_records(domain)
        spf_records = [record for record in txt Records if record.startswith('v=spf1')]
        return spf_records
    except Exception as e:
        print(f"Error gathering SPF records: {e}")
        return []

def gather_subdomains(domain):
    """Gather subdomains using a simple approach (can be enhanced with tools like sublist3r)."""
    try:
        # This is a basic implementation; consider integrating external tools for better results
        subdomains = []
        # Add logic to enumerate subdomains (e.g., using brute force or existing tools)
        return subdomains
    except Exception as e:
        print(f"Error gathering subdomains: {e}")
        return []

def perform_domain_reconnaissance(domain):
    """Perform comprehensive domain reconnaissance and store results."""
    global knowledge_base
    
    # Initialize domain info
    domain_info = {
        'Domain': domain,
        'Timestamp': datetime.now().isoformat(),
        'DNS Records': {},
        'WHOIS Information': '',
        'MX Records': [],
        'TXT Records': [],
        'SPF Records': [],
        'Subdomains': []
    }
    
    # Gather DNS information
    dns_info = gather_dns_information(domain)
    if dns_info:
        domain_info['DNS Records'].update(dns_info)
        
    # Gather WHOIS information
    whois_info = gather_whois_information(domain)
    if whois_info:
        domain_info['WHOIS Information'] = whois_info
        
    # Gather MX records
    mx_records = gather_mx_records(domain)
    if mx_records:
        domain_info['MX Records'] = mx_records
        
    # Gather TXT records
    txt_records = gather_txt_records(domain)
    if txt_records:
        domain_info['TXT Records'] = txt_records
        
    # Gather SPF records
    spf_records = gather_spf_records(domain)
    if spf_records:
        domain_info['SPF Records'] = spf_records
        
    # Gather subdomains (enhance this part with a better enumeration method)
    subdomains = gather_subdomains(domain)
    if subdomains:
        domain_info['Subdomains'] = subdomains
        
    # Save to knowledge base
    knowledge_base[domain] = domain_info
    
    # Save to JSON file
    try:
        with open(f"reconnaissance_{datetime.now().strftime('%Y%m%d%H%M%S')}.json", 'w') as f:
            json.dump(domain_info, f, indent=4)
        print("Domain reconnaissance data saved to file.")
    except Exception as e:
        print(f"Error saving domain reconnaissance data: {e}")

if __name__ == "__main__":
    # Example usage
    domain = "example.com"
    perform_domain_reconnaissance(domain)
    
    # Access the knowledge base
    if domain in knowledge_base:
        print("Domain Reconnaissance Summary:")
        print(json.dumps(knowledge_base[domain], indent=4))