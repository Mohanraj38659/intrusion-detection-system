from detector import IntrusionDetector
from logger import Logger
from network_monitor import NetworkMonitor

def main():
    detector = IntrusionDetector(threshold=120)
    
    print("Monitoring Network Traffic...")
    packet_count = NetworkMonitor.get_packet_count()
    
    result = detector.analyze_traffic(packet_count)
    Logger.log(f"Packets: {packet_count}, Status: {result}")

if __name__ == "__main__":
    main()
