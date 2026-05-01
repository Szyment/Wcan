# to steruje programem
from network import generate_ips
from scanner import scan_hosts
from tyler import get_hostname, get_mac
from storage import create_scan_object, save_scan
from szalonyreporter import show_report


try:
    cidr = input("Podaj CIDR sieci: ").strip()

    hosts = generate_ips(cidr)
    print(f"Wygenerowano {len(hosts)} adresów IP.")

    results = scan_hosts(hosts)

    for result in results:
        if result["status"] == "up":
            ip = result["ip"]

            result["hostname"] = get_hostname(ip)
            result["mac"] = get_mac(ip)
            result["open_ports"] = []

        else:
            result["hostname"] = None
            result["mac"] = None
            result["open_ports"] = []

    scan = create_scan_object(
        target=cidr,
        results=results
    )

    file_path = save_scan(scan)

    show_report(scan)

    print()
    print(f"Zapisano skan do: {file_path}")

except ValueError:
    print("Błąd: podano niepoprawny CIDR.")