import sys

try:
    import psutil
except ImportError:
    print("Error: psutil module is not installed. Install it with 'pip install psutil'.")
    sys.exit(1)

import socket

print("🌐 Network Interfaces\n")

addrs = psutil.net_if_addrs()

for iface, snics in addrs.items():
    print(f"{iface}")

    ip_found = False
    for snic in snics:
        if snic.family == socket.AF_INET:
            print("  IP:", snic.address)
            ip_found = True

    if not ip_found:
        print("  IP: not assigned")

    print("-" * 30)