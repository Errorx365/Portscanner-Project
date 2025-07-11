#!/usr/bin/env python3

import socket
import argparse
from datetime import datetime

def scan_target(target, ports):
    print(f"\n[*] Starting scan on {target}")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Scan cancelled by user.")
            break
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            break
        except socket.error:
            print("[!] Couldn't connect to server.")
            break

def get_port_list(port_range):
    ports = []
    if "-" in port_range:
        start, end = map(int, port_range.split("-"))
        ports = list(range(start, end + 1))
    else:
        ports = list(map(int, port_range.split(",")))
    return ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", help="Port(s) to scan (e.g. 22,80,443 or 1-1000)", default="1-1024")

    args = parser.parse_args()
    target_ip = socket.gethostbyname(args.target)
    port_list = get_port_list(args.ports)

    print("="*50)
    print(f"Scanning Target: {args.target} ({target_ip})")
    print(f"Time Started: {datetime.now()}")
    print("="*50)

    scan_target(target_ip, port_list)
