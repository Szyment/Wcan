# ping + port scan
import platform
import subprocess


def ping_host(ip):
    system_name = platform.system().lower()

    if system_name == "windows":
        command = ["ping", "-n", "1", ip]
    else:
        command = ["ping", "-c", "1", ip]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=0.5
        )

        return result.returncode == 0

    except subprocess.TimeoutExpired:
        return False


def scan_hosts(hosts):
    results = []

    for ip in hosts:
        is_up = ping_host(ip)

        result = {
            "ip": ip,
            "status": "up" if is_up else "no_response"
        }

        results.append(result)

    return results