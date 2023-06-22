import argparse
import socket
from rich.console import Console
from rich.table import Table
from scapy.all import ARP, Ether, srp
import requests
import threading
import time

console = Console()

def get_arguments():
    parser = argparse.ArgumentParser(description='Network Scanner Tool')
    parser.add_argument("-t", "--target", metavar="", help="Target IP address or subnet (default: 192.168.1.0/24)", default="192.168.1.0/24")
    parser.add_argument("-i", "--interface", metavar="", help="Interface to use (default: None)", default=None)
    parser.add_argument("-l", "--live", action="store_true", help="Enable live tracking of devices")
    parser.add_argument("-o", "--output", metavar="", help="Output file to save the results")
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
        devices.append({'ip': received.psrc, 'mac': mac_address, 'manufacturer': manufacturer})

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


def display_live_updates(target, iface):
    while True:
        devices = scan(target, iface)

        console.clear()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("IP Address", style="bold red")
        table.add_column("MAC Address", style="bold blue")
        table.add_column("Manufacturer", style="bold yellow")

        for device in devices:
            table.add_row(device['ip'], device['mac'], device['manufacturer'])

        console.print(table)
        time.sleep(5)


def save_results(devices, output_file):
    with open(output_file, 'w') as f:
        for device in devices:
            f.write(f"IP Address: {device['ip']}\n")
            f.write(f"MAC Address: {device['mac']}\n")
            f.write(f"Manufacturer: {device['manufacturer']}\n")
            f.write("\n")


def main():
    try:
        args = get_arguments()
        target = args.target
        iface = args.interface
        live_tracking = args.live
        output_file = args.output

        devices = scan(target, iface)

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("IP Address", style="bold red")
        table.add_column("MAC Address", style="bold blue")
        table.add_column("Manufacturer", style="bold yellow")

        for device in devices:
            table.add_row(device['ip'], device['mac'], device['manufacturer'])

        console.print(table)

        if output_file:
            save_results(devices, output_file)
            console.print(f"\n[bold green]Results saved to: {output_file}")

        if live_tracking:
            t = threading.Thread(target=display_live_updates, args=(target, iface))
            t.daemon = True  # This makes sure the thread will exit when the main program exits
            t.start()
            while t.is_alive():  # This loop will keep the main thread running while the display thread is running
                time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[bold red]Program interrupted by user. Exiting...")


if __name__ == "__main__":
    main()
