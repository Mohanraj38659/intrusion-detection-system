import random

class NetworkMonitor:
    @staticmethod
    def get_packet_count():
        return random.randint(50, 200)  # Simulates random network traffic
