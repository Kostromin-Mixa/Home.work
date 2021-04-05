#!/usr/bin/env python3
import socket
a = socket.gethostbyname('drive.google.com')
b = socket.gethostbyname('mail.google.com')
c = socket.gethostbyname('google.com')
host_a = [a]
host_ab = []
if host_a != host_ab:
    print("ERROR drive.google.com IP mismatch:", host_ab, a)
else:
    print("drive.google.com", a)
host_ab = [a]

host_b = [b]
host_bb = []
if host_b != host_bb:
    print("ERROR mail.google.com IP mismatch:", host_bb, b)
else:
    print("mail.google.com", b)
host_bb = [b]

host_c = [c]
host_cb = []
if host_c != host_cb:
    print("ERROR google.com IP mismatch:", host_cb, c)
else:
    print("drive.google.com", c)
host_cb = [c]