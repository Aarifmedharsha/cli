class Device:
    def __init__(self, device_type, name):
        self.device_type = device_type
        self.name = name
        self.strength = 5
        self.adjacent = []
