import pyfiglet
import scapy.all as scapy
import re

# Wifi Scanner by Mr-Cuda
title = pyfiglet.figlet_format("WiFi Scanner")
print(title)

ipRegex = re.compile("^(?:[0-9]{1,3]\.){3}[0-9]{1,3}/[0-9]*$")

ipAddrRange = input("Please enter a valid aip adress range: ")

if ipRegex.search(ipAddrRange):
  print(f"{ipAddrRange} is a valid ip addres range")

result = scapy.arping(ipAddrRange)
