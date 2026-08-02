import socket
import requests
import sys
from datetime import datetime

class EthicalHackerTool:
    def __init__(self, target_domain):
        self.target = target_domain
        try:
            self.target_ip = socket.gethostbyname(target_domain)
        except socket.gaierror:
            print("\n🛑 [ERROR] Could not resolve hostname. Please enter a valid domain!")
            sys.exit()

    def print_banner(self):
        print("=" * 60)
        print(f"🕵️‍♂️ ADVANCED ETHICAL HACKING & PENETRATION TESTING TOOL")
        print(f"🎯 Target Host: {self.target} ({self.target_ip})")
        print(f"⏰ Operation Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)

    # 1. Banner Grabbing (Information Gathering / Footprinting)
    def banner_grabbing(self):
        print("\n[+] Phase 1: Performing Banner Grabbing (Information Gathering)...")
        ports = [21, 22, 80]  # Standard ports for FTP, SSH, and HTTP
        
        for port in ports:
            try:
                s = socket.socket()
                s.settimeout(2.0)
                s.connect((self.target_ip, port))
                
                # If checking HTTP port, send a basic request to trigger a banner response
                if port == 80:
                    s.sendall(b"GET / HTTP/1.1\r\nHost: " + self.target.encode() + b"\r\n\r\n")
                
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"  🚨 Banner Found on Port {port}: \n{banner[:150]}...")
            except:
                print(f"  ✅ Port {port}: Secure or banner information is hidden by the server.")
            finally:
                s.close()

    # 2. Subdomain Enumeration (Discovering Hidden Assets)
    def find_subdomains(self):
        print("\n[+] Phase 2: Active Subdomain Discovery (Reconnaissance)...")
        # List of common subdomains to check
        common_subdomains = ["admin", "mail", "dev", "test", "api", "vpn"]
        
        for sub in common_subdomains:
            sub_domain = f"{sub}.{self.target}"
            try:
                sub_ip = socket.gethostbyname(sub_domain)
                print(f"  🚨 Subdomain Discovered: http://{sub_domain} (IP: {sub_ip})")
            except socket.gaierror:
                pass  # Subdomain does not exist, move to the next one

if __name__ == "__main__":
    # For safety and legal compliance, test using 'localhost' or authorized domains like 'example.com'
    target = input("Enter target domain for ethical testing (e.g., example.com): ")
    hacker = EthicalHackerTool(target)
    hacker.print_banner()
    hacker.banner_grabbing()
    hacker.find_subdomains()
    print("\n" + "=" * 60)
    print("🔒 RECON COMPLETE: Upload this repository to GitHub for university admissions review.")
    print("=" * 60)
