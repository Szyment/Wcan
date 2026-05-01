# generuje zakres ip
from ipaddress import ip_network


def generate_ips(cidr):
    network = ip_network(cidr, strict=False)

    hosts = []

    for ip in network.hosts():
        hosts.append(str(ip))

    return hosts