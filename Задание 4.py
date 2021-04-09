#!/usr/bin/env python3
import socket

hosts = ['drive.google.com', 'mail.google.com', 'google.com']
ips = {}
for host in hosts:
    ips[host] = socket.gethostbyname(host)

while True:
    for host in hosts:
        oldip = ips[host]
        newip = socket.gethostbyname(host)

        if (oldip != newip):
            print("ERROR", host, "IP mismatch:", oldip, newip)

        else:
            print(host, newip)
    import time
    time.sleep(3) # 3 seconds



