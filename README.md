# NetProbe: Network Probe
This program is a tool you can use to scan for devices on your network. The program sends ARP requests to any IP address on your network and lists the IP addresses, MAC addresses, and device names of the responding devices.

## Download

You can download the program from the GitHub page.

```bash
git clone https://github.com/HalilDeniz/Network-Scanner.git
```

## Installation

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the program, use the following command:

```bash
python3 network-scnner.py -t [target] -i [interface]
```

- `[target]`: IP address or subnet to scan (default: 192.168.1.0/24)
- `[interface]`: Interface to use (default: None)

Example:

```bash
python3 network-scanner.py -t 192.168.1.0/24 -i eth0
```

## Features

The program lists the IP addresses, MAC addresses, and device names of the devices on your network. You can get an example output like the following:

```
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ IP Address   ┃ MAC Address       ┃ Device Name     ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ 192.168.1.1  │ b0:**:bf:**:32:** │ router.****.com │
│ 192.168.1.2  │ d4:**:64:**:5c:** │ Unknown         │
│ 192.168.1.6  │ **:5e:**:16:**:** │ Unknown         │
│ 192.168.1.25 │ 0a:**:50:00:**:** │ Unknown         │
└──────────────┴───────────────────┴─────────────────┘
```
## Contributing
Contributions are welcome! To contribute to Network-Scanner, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request in the main repository.



## Contact
If you have any questions, suggestions, or feedback about the program, please feel free to reach out to me through any of the following platforms:


- LinkedIn: https://www.linkedin.com/in/halil-ibrahim-deniz/
- TryHackMe: https://tryhackme.com/p/halilovic
- Instagram: https://www.instagram.com/deniz.halil333/
- YouTube: https://www.youtube.com/c/HalilDeniz
- Email: halildeniz313@gmail.com

## License

This program is released under the MIT License. See LICENSE for more information.
