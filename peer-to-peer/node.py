class Node:
    def __init__(self, name):
        self.name = name
        self.peers = []

    def add_peer(self, peer):
        self.peers.append(peer)

    def send_message(self, message):
        for peer in self.peers:
            peer.receive_message(message)

    def receive_message(self, message):
        print(f"{self.name} received message: {message}")
