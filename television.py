class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

def __init__(self):
    self.status = False
    self.muted = False
    self.volume = self.min_volume
    self.channel = self.min_channel
