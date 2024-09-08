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

# Iconos Nerd Fonts
ICON_LINUX = "\ue712"  # Icono de pingüino (Linux)
ICON_WINDOWS = "\uf17a"  # Icono de Windows
ICON_NOT_FOUND = "\uf002"  # Icono de lupa

# Función para mostrar la ayuda
def print_help():
    help_text = """
Uso:
    python3 {} <direccion-ip>
    
Descripción:
    Este script intenta identificar el sistema operativo de un dispositivo remoto
    basado en el valor TTL de una solicitud de ping.

Opciones:
    -h, --help    Muestra esta ayuda y sale.

Ejemplo:
    python3 {} 192.168.1.1

Salida:
    Se mostrará la dirección IP, el TTL y el sistema operativo (Linux, Windows o no encontrado)
    junto con un icono y color asociado.
    """.format(sys.argv[0], sys.argv[0])
    print(help_text)
    sys.exit(0)

# Verifica si se pasa el argumento de ayuda
if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
    print_help()

# Función para obtener el TTL
def get_ttl(ip_address):
    try:
        proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        out = out.split()
        out = out[12].decode('utf-8')

        ttl_value = re.findall(r"\d{1,3}", out)[0]

        return ttl_value
    except Exception as e:
        print(f"\n[!] Error al obtener el TTL para {ip_address}: {e}\n")
        sys.exit(1)

# Función para determinar el sistema operativo según el TTL
def get_os(ttl):
    ttl = int(ttl)

    if ttl >= 0 and ttl <= 64:
        return "Linux", ICON_LINUX, COLOR_YELLOW  # Linux
    elif ttl >= 65 and ttl <= 128:
        return "Windows", ICON_WINDOWS, COLOR_BLUE  # Windows
    else:
        return "Not Found", ICON_NOT_FOUND, COLOR_RED  # No encontrado

if __name__ == '__main__':
    ip_address = sys.argv[1]

    ttl = get_ttl(ip_address)
    os_name, os_icon, color = get_os(ttl)

    # Mostrar la información con el color y el icono
    print("\n{} (ttl -> {}): {} {}{}{}\n".format(ip_address, ttl, color, os_name, os_icon, COLOR_RESET))
