#hostname + MAC
import re
import socket
import subprocess


def get_hostname(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return None


def get_mac(ip):
    try:
        result = subprocess.run(
            ["arp", "-a"],
            capture_output=True,
            text=True,
            timeout=2
        )

        output = result.stdout

        pattern = rf"\({re.escape(ip)}\)\s+at\s+([0-9a-fA-F:]+)"
        match = re.search(pattern, output)

        if match:
            return match.group(1).lower()

        return None

    except subprocess.TimeoutExpired:
        return None