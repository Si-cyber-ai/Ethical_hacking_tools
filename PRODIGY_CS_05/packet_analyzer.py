print("============================== Network Packet Analyzer================================ ")

from scapy.all import sniff

def display_disclaimer():
    print("DISCLAIMER:")
    print("Using packet sniffing tools to capture network packets may have legal and ethical ramifications.")
    print("By utilizing this tool, you acknowledge and agree to the following terms and conditions:")
    print("1. You confirm that you have obtained explicit permission from relevant authorities to capture and analyze network traffic on the network you are connected to.")
    print("2. You agree to utilize this packet sniffer solely for educational purposes, network troubleshooting, or cybersecurity training.")
    print("3. You are responsible for ensuring that your use of this tool complies with all applicable laws and regulations concerning data privacy and network monitoring.")
    print("4. You will not use this tool to access, capture, or analyze data without appropriate authorization.")
    print("5. The creators and contributors of this tool are not responsible for any consequences arising from its use.")
    print("6. You agree to respect the privacy of all individuals on the network.")
    print()
    acceptance = input("Do you accept these terms and conditions? (yes/no): ").strip().lower()
    return acceptance == 'yes'

# Function to handle captured packets
def process_packet(packet):
    try:
        
        # Extract key information from the packet
        ip_src = packet[1].src  # Source IP address
        ip_dst = packet[1].dst  # Destination IP address
        protocol = packet[1].proto  # Protocol used
        payload = bytes(packet[1].payload)  # Data payload

        # Print the packet details
        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {protocol}, Payload: {payload[:50]}")
    except IndexError:
        # Skip packets that do not contain IP information
        pass

# Main body
if display_disclaimer():
    print("Initiating packet sniffer... Press Ctrl+C to stop.")
    # Start capturing packets and process each one using process_packet
    sniff(prn=process_packet, store=False)
else:
    print("You must accept the terms to use this tool. Exiting...")
