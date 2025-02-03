class IntrusionDetector:
    def __init__(self, threshold=100):
        self.threshold = threshold  # Example threshold for suspicious activity

    def analyze_traffic(self, packet_count):
        if packet_count > self.threshold:
            return "Intrusion Detected!"
        return "Normal Traffic"
