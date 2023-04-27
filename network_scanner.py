import argparse
import socket
from rich.console import Console
from rich.table import Table
from scapy.all import ARP, Ether, srp

console = Console()

def get_arguments():
    parser = argparse.ArgumentParser(description='Network Scanner Tool',
                                     epilog='''Example Uses:
    python network_scanner.py -h
    python network_scanner.py -t 192.168.1.0/24
    python network_scanner.py -t 10.0.0.0/24 -i eth0
    python network_scanner.py -t 192.168.1.100
    python network_scanner.py -t 192.168.1.0/24 > devices.txt
    ''', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-t", "--target", metavar="", help="Target IP address or subnet (default: 192.168.1.0/24)", default="192.168.1.0/24")
    parser.add_argument("-i", "--interface", metavar="", help="Interface to use (default: None)", default=None)
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
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def get_device_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return "Unknown"

def main():
    args = get_arguments()
    target = args.target
    iface = args.interface

    devices = scan(target, iface)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("IP Address", style="bold red")
    table.add_column("MAC Address", style="bold blue")
    table.add_column("Device Name", style="bold green")

    for device in devices:
        device_name = get_device_name(device['ip'])
        table.add_row(device['ip'], device['mac'], device_name)

    console.print(table)

if __name__ == "__main__":
    main()
