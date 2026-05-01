#pokazuje wynik
# pokazuje wynik
def show_report(scan):
    print()
    print("=== REPORT ===")
    print(f"Target: {scan['target']}")
    print(f"Created at: {scan['created_at']}")
    print(f"Hosts scanned: {scan['summary']['hosts_scanned']}")
    print(f"Hosts up: {scan['summary']['hosts_up']}")

    print()
    print("=== DEVICES UP ===")

    found_any = False

    for device in scan["devices"]:
        if device["status"] == "up":
            found_any = True

            print()
            print(f"+ {device['ip']}")
            print(f"  status: {device['status']}")
            print(f"  hostname: {device.get('hostname')}")
            print(f"  mac: {device.get('mac')}")
            print(f"  open_ports: {device.get('open_ports', [])}")

    if not found_any:
        print("No responding hosts.")

    print()
    print("=== NO RESPONSE ===")

    no_response_count = 0

    for device in scan["devices"]:
        if device["status"] == "no_response":
            no_response_count += 1

    print(f"No response hosts: {no_response_count}")