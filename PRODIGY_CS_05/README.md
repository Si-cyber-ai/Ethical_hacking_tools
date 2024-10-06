# Network Packet Analyzer

This is a simple yet powerful tool for capturing and analyzing network packets in real-time using Python and the Scapy library. The Network Packet Analyzer allows users to monitor network traffic, identify potential security threats, and understand data flow within their networks.

## Features

- **Real-Time Packet Sniffing**: Captures and analyzes packets as they traverse the network.
- **Detailed Packet Information**: Displays source IP, destination IP, protocol, and payload data for each packet.
- **User-Friendly Interface**: Provides clear prompts and outputs for easy interaction.

## How It Works

1. **Input**: The user is prompted to accept the terms and conditions for using the packet sniffer.
2. **Processing**:
   - Once accepted, the program starts capturing network packets.
   - For each captured packet, it extracts relevant information such as source and destination IP addresses, the protocol used, and the payload data.
3. **Output**: The program outputs the details of each captured packet in real-time.

## Installation and Usage

### Prerequisites

- **Python 3.x** installed on your system.
- **Scapy library** for packet analysis.

### Running the Network Packet Analyzer

1. Clone or download this repository.
2. Open a terminal or command prompt in the project directory.
3. Install Scapy using pip:

    ```bash
    pip install scapy
    ```

4. Run the Python file:

    ```bash
    python network_packet_analyzer.py
    ```

5. Follow the prompts to accept the terms and conditions, and the packet sniffer will start capturing packets.

## Example Usage

```plaintext
=============================== Network Packet Analyzer =================================
DISCLAIMER:
Using packet sniffing tools to capture network packets may have legal and ethical ramifications.
Do you accept these terms and conditions? (yes/no): yes
Initiating packet sniffer... Press Ctrl+C to stop.
Source IP: 192.168.1.10, Destination IP: 192.168.1.20, Protocol: 6, Payload: b'GET /index.html HTTP/1.1'
```

## Future Improvements

- **Enhanced Filtering Options**: Allow users to filter packets based on criteria such as source/destination IP or protocol.
- **Graphical User Interface (GUI)**: Develop a GUI for easier interaction and visualization of captured packets.
- **Export Functionality**: Implement a feature to export captured packet data to a file for further analysis.

## Credits

Developed by **Sidharth P Nair**

---

**Important**: Please use this tool responsibly and ensure you have permission to analyze the network traffic in your environment. Packet sniffing can have legal and ethical implications.
