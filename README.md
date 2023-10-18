# NetProbe: Network Probe

This program is a tool you can use to scan for devices on your network. The program sends ARP requests to any IP address on your network and lists the IP addresses, MAC addresses, manufacturers, and device models of the responding devices.

## Features

- Scan for devices on a specified IP address or subnet
- Display the IP address, MAC address, manufacturer, and device model of discovered devices
- Live tracking of devices (optional)
- Save scan results to a file (optional)


## Download

You can download the program from the GitHub page.
```bash
git clone https://github.com/HalilDeniz/NetProbe.git
```

## Installation

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the program, use the following command:

```bash
python3 netprobe.py -t [target] -i [interface] -o [output_file] -l
```

- `[target]`: Target IP address or subnet (default: 192.168.1.0/24)
- `[interface]`: Interface to use (default: None)
- `[output_file]`: Output file to save the results (optional)
- `-l` or `--live`: Enable live tracking of devices

## Example:

```bash
python3 netrobe.py -t 192.168.1.0/24 -i eth0 -o results.txt -l
```
## Help Menu
```
python3 network_scanner.py --help
usage: network_scanner.py [-h] [-t] [-i] [-l] [-o]

Network Scanner Tool

options:
  -h, --help         show this help message and exit
  -t , --target      Target IP address or subnet (default: 192.168.1.0/24)
  -i , --interface   Interface to use (default: None)
  -l, --live         Enable live tracking of devices
  -o , --output      Output file to save the results
```                                               


## Default Scan

```bash
python3 netprobe.py 
```

## Live Tracking

You can enable live tracking of devices on your network by using the `-l` or `--live` flag. This will continuously update the device list every 5 seconds.

```
python3 network-scanner.py -t 192.168.1.0/24 -i eth0 -l
```

## Save Results
You can save the scan results to a file by using the `-o` or `--output` flag followed by the desired output file name.
```
python3 netprobe.py -t 192.168.1.0/24 -i eth0 -o results.txt
```



```
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ IP Address   ┃ MAC Address       ┃ Manufacturer          ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 192.168.1.1  │ b0:**:bf:**:32:** │ ASUSTek COMPUTER INC. │
│ 192.168.1.25 │ **:49:**:00:**:38 │ OPPO Digital, Inc.    │
│ 192.168.1.98 │ d4:**:64:**:5c:** │ ASUSTek COMPUTER INC. │
│ 192.168.1.4  │ **:02:**:5b:**:65 │ LG Innotek            │
└──────────────┴───────────────────┴───────────────────────┘
```

## Contact
If you have any questions, suggestions, or feedback about the program, please feel free to reach out to me through any of the following platforms:



- Mywebsite: [Denizhalil](https://denizhalil.com)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/halil-ibrahim-deniz/)
- TryHackMe: [TryHackMe](https://tryhackme.com/p/halilovic)
- Instagram: [Instagram](https://www.instagram.com/deniz.halil333/)
- YouTube: [YouTube](https://www.youtube.com/c/HalilDeniz)
- Email: halildeniz313@gmail.com


## License

This program is released under the MIT License. See LICENSE for more information.
