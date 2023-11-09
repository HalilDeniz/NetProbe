#!/usr/bin/env python3

import argparse
from rich.console import Console
from rich.table import Table
from scapy.all import ARP, Ether, srp
import requests
import threading
import time

console = Console()

def get_arguments():
    parser = argparse.ArgumentParser(description='NetProbe: Network Scanner Tool')
    parser.add_argument("-t", "--target", metavar="", help="Target IP address or subnet (default: 192.168.1.0/24)", default="192.168.1.0/24", nargs='+', required=True)
    parser.add_argument("-i", "--interface", metavar="", help="Interface to use (default: None)", default=None, nargs='+', required=True)
    parser.add_argument("-l", "--live", action="store_true", help="Enable live tracking of devices")
    parser.add_argument("-o", "--output", metavar="", help="Output file to save the results")
    parser.add_argument("-m", "--manufacturer", metavar="", help="Filter by manufacturer (e.g., 'Apple')")
    parser.add_argument("-r", "--ip-range", metavar="", help="Filter by IP range (e.g., '192.168.1.0/24')")
    parser.add_argument("-s", "--scan-rate", metavar="", help="Scan rate in seconds (default: 5)", type=int, default=5)
    return parser.parse_args()

def scan(target, iface):
    arp = ARP(pdst=target)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    try:
        result = srp(packet, timeout=3, verbose=0, iface=iface)[0]
    except PermissionError:
        console.print("[bold red]Error:[/] You do not have sufficient privileges. Try running the program with 'sudo'.")
        exit()
    except OSError as e:
        if "No such device" in str(e):
            console.print(f"[bold red]Error:[/] Interface '{iface}' does not exist. \nPlease provide a valid interface name.")
            exit()
        else:
            raise

    devices = []
    for sent, received in result:
        mac_address = received.hwsrc
        manufacturer = get_device_info(mac_address)
        packet_size = len(sent) + len(received)
        devices.append({'ip': received.psrc, 'mac': mac_address, 'manufacturer': manufacturer, 'packet_size': packet_size})

    return devices

def get_device_info(mac_address):
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url)
        if response.status_code == 200:
            manufacturer = response.text.strip()
        else:
            manufacturer = "Unknown"
    except requests.exceptions.RequestException:
        manufacturer = "Unknown"

    return manufacturer

def apply_filters(devices, manufacturer_filter, ip_range_filter):
    filtered_devices = []
    for device in devices:
        if (not manufacturer_filter or device['manufacturer'].lower() == manufacturer_filter.lower()) and (not ip_range_filter or ip_in_range(device['ip'], ip_range_filter)):
            filtered_devices.append(device)
    return filtered_devices

def ip_in_range(ip, ip_range):
    try:
        ip_network = ip_range.split('/')[0]
        subnet_mask = int(ip_range.split('/')[1])
        return ipaddress.ip_address(ip) in ipaddress.ip_network(ip_network, strict=False)
    except ValueError:
        return False

def display_live_updates(targets, interfaces, output_file=None, manufacturer_filter=None, ip_range_filter=None, scan_rate=5):
    known_devices = []
    while True:
        for target in targets:
            for iface in interfaces:
                devices = scan(target, iface)

                # Save newly discovered devices
                new_devices = [d for d in devices if d not in known_devices]
                if new_devices and output_file:
                    save_results(new_devices, output_file)
                    known_devices.extend(new_devices)

                filtered_devices = apply_filters(devices, manufacturer_filter, ip_range_filter)

                console.clear()
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("IP Address", style="bold red")
                table.add_column("MAC Address", style="bold blue")
                table.add_column("Packet Size", style="bold green")
                table.add_column("Manufacturer", style="bold yellow")

                for device in filtered_devices:
                    table.add_row(device['ip'], device['mac'], str(device['packet_size']), device['manufacturer'])

                console.print(table)
                time.sleep(scan_rate)

def save_results(devices, output_file):
    with open(output_file, 'a') as f:  # 'a' for append mode
        for device in devices:
            f.write(f"IP Address: {device['ip']}\n")
            f.write(f"MAC Address: {device['mac']}\n")
            f.write(f"Manufacturer: {device['manufacturer']}\n")
            f.write(f"Packet Size: {device['packet_size']} bytes\n")
            f.write("\n")

def main():
    try:
        args = get_arguments()
        targets = args.target
        interfaces = args.interface
        live_tracking = args.live
        output_file = args.output
        manufacturer_filter = args.manufacturer
        ip_range_filter = args.ip_range
        scan_rate = args.scan_rate

        devices = []
        for target in targets:
            for iface in interfaces:
                devices.extend(scan(target, iface))

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("IP Address", style="bold red")
        table.add_column("MAC Address", style="bold blue")
        table.add_column("Packet Size", style="bold green")
        table.add_column("Manufacturer", style="bold yellow")

        filtered_devices = apply_filters(devices, manufacturer_filter, ip_range_filter)

        for device in filtered_devices:
            table.add_row(device['ip'], device['mac'], str(device['packet_size']), device['manufacturer'])

        console.print(table)

        if output_file:
            save_results(filtered_devices, output_file)
            console.print(f"\n[bold green]Results saved to: {output_file}")

        if live_tracking:
            t = threading.Thread(target=display_live_updates, args=(targets, interfaces, output_file, manufacturer_filter, ip_range_filter, scan_rate))
            t.daemon = True  # This makes sure the thread will exit when the main program exits
            t.start()
            while t.is_alive():  # This loop will keep the main thread running while the display thread is running
                time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[bold red]Program interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
