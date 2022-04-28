#! /usr/bin/python 

# Name: .py
# Author: Joe Bloggs
# Revision: v1.0
# Description: Program Description
"""
    Docstring contents here
"""

import pickle
import re
import platform

if "Windows" or "windows" in platform.system:
    filename = r"C:\WINDOWS\System32\drivers\etc\services"
else:
    filename = r"/etc/services"

all_ports = set(range(1, 201))
used_ports = set()
port_pattern = re.compile(r"\s(([1]?[0-9]{1,2})|(200))/(udp|tcp)")

with open(filename, "rt") as fh_in:
    for lines in fh_in:
        line = re.search(port_pattern, lines)
        if line:
            used_ports.add(int(line.group(1)))
            print(line.group(1))
print(all_ports - used_ports)


