#!/usr/bin/python3
# coding: utf-8

import re
import sys
import subprocess

# Secuencias ANSI para colores
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

# python3 wichSystem.py 10.10.10.188

if len(sys.argv) != 2:
    print("\n[!] Uso: python3 " + sys.argv[0] + " <direccion-ip>\n")
    sys.exit(1)

def get_ttl(ip_address):
    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    out = out.split()
    out = out[12].decode('utf-8')

    ttl_value = re.findall(r"\d{1,3}", out)[0]

    return ttl_value

def get_os(ttl):
    ttl = int(ttl)

    if ttl >= 0 and ttl <= 64:
        return "Linux", "\ue712", COLOR_YELLOW  # Icono de pingüino (Linux), color amarillo
    elif ttl >= 65 and ttl <= 128:
        return "Windows", "\uf17a", COLOR_BLUE  # Icono de Windows, color azul
    else:
        return "Not Found", "\uf002", COLOR_RED  # Icono de lupa, color rojo

if __name__ == '__main__':
    ip_address = sys.argv[1]

    ttl = get_ttl(ip_address)
    os_name, os_icon, color = get_os(ttl)
    print("\n%s (ttl -> %s): %s %s%s%s\n" % (ip_address, ttl, os_name, color, os_icon, COLOR_RESET))