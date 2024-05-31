# NetProbe: Network Probe

**NetProbe** is a tool you can use to scan for devices on your network. The program sends ARP requests to any IP address on your network and lists the IP addresses, MAC addresses, manufacturers, and device models of the responding devices.

<h4 align="center">
<br>
   <a href="https://buymeacoffee.com/halildeniz" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</h4>


## Features

- Scan for devices on a specified IP address or subnet
- Display the IP address, MAC address, manufacturer, and device model of discovered devices
- Live tracking of devices (optional)
- Save scan results to a file (optional)
- Filter by manufacturer (e.g., 'Apple') (optional)
- Filter by IP range (e.g., '192.168.1.0/24') (optional)
- Scan rate in seconds (default: 5) (optional)

## Download

You can download the program from the GitHub page.
```bash
$ git clone https://github.com/HalilDeniz/NetProbe.git
```

## Installation

To install the required libraries, run the following command:

```bash
$ pip install -r requirements.txt
```

## Usage

To run the program, use the following command:

```bash
$ python3 netprobe.py [-h] -t  [...] -i  [...] [-l] [-o] [-m] [-r] [-s]
```

- `-h`,`--help`: show this help message and exit
- `-t`,`--target`: Target IP address or subnet (default: 192.168.1.0/24)
- `-i`,`--interface`: Interface to use (default: None)
- `-l`,`--live`: Enable live tracking of devices
- `-o`,`--output`: Output file to save the results
- `-m`,`--manufacturer`: Filter by manufacturer (e.g., 'Apple')
- `-r`,`--ip-range`: Filter by IP range (e.g., '192.168.1.0/24')
- `-s`,`--scan-rate`: Scan rate in seconds (default: 5)

## Example:

```shell
$ python3 netprobe.py -t 192.168.1.0/24 -i eth0 -o results.txt -l
```
## Help Menu
```shell
$ python3 netprobe.py --help                      
usage: netprobe.py [-h] -t  [...] -i  [...] [-l] [-o] [-m] [-r] [-s]

NetProbe: Network Scanner Tool

options:
  -h, --help            show this help message and exit
  -t  [ ...], --target  [ ...]
                        Target IP address or subnet (default: 192.168.1.0/24)
  -i  [ ...], --interface  [ ...]
                        Interface to use (default: None)
  -l, --live            Enable live tracking of devices
  -o , --output         Output file to save the results
  -m , --manufacturer   Filter by manufacturer (e.g., 'Apple')
  -r , --ip-range       Filter by IP range (e.g., '192.168.1.0/24')
  -s , --scan-rate      Scan rate in seconds (default: 5)

```                                               


## Default Scan

```bash
$ python3 netprobe.py 
```

## Live Tracking

You can enable live tracking of devices on your network by using the `-l` or `--live` flag. This will continuously update the device list every 5 seconds.

```shell
$ python3 netprobe.py -t 192.168.1.0/24 -i eth0 -l
```

## Save Results
You can save the scan results to a file by using the `-o` or `--output` flag followed by the desired output file name.
```
$ python3 netprobe.py -t 192.168.1.0/24 -i eth0 -l -o results.txt
```

```shell
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ IP Address   ┃ MAC Address       ┃ Packet Size ┃ Manufacturer                 ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 192.168.1.1  │ **:6e:**:97:**:28 │ 102         │ ASUSTek COMPUTER INC.        │
│ 192.168.1.3  │ 00:**:22:**:12:** │ 102         │ InPro Comm                   │
│ 192.168.1.2  │ **:32:**:bf:**:00 │ 102         │ Xiaomi Communications Co Ltd │
│ 192.168.1.98 │ d4:**:64:**:5c:** │ 102         │ ASUSTek COMPUTER INC.        │
│ 192.168.1.25 │ **:49:**:00:**:38 │ 102         │ Unknown                      │
└──────────────┴───────────────────┴─────────────┴──────────────────────────────┘
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

This program is released under the MIT [LICENSE](LICENSE). See LICENSE for more information.

## 💰 You can help me by Donating
Thank you for considering supporting me! Your support enables me to dedicate more time and effort to creating useful tools like DNSWatch and developing new projects. By contributing, you're not only helping me improve existing tools but also inspiring new ideas and innovations. Your support plays a vital role in the growth of this project and future endeavors. Together, let's continue building and learning. Thank you!"
[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/halildeniz) 
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/denizhalil) 

  
