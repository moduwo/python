class Television:
    min_volume:int = 0
    max_volume:int = 2
    min_channel:int = 0
    max_channel:int = 3

    def __init__(self) -> None:
        "Instance Variables"
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel

    def power(self) -> None:
        "Should return True if power is on and should return False if off"
        if self.__status:
            self.__status = False
        else:
            self.__status = True
        return self.__status

    def mute(self) -> None:
        "Volume should return 0 if muted"
        if self.__muted:
            self.__muted = True
        if True:
            self.__volume = self.min_volume
        return self.__volume

    def channel_up(self) -> None:
        "Channel number should increase unless it is the max"
        if self.__status:
            if self.__channel == self.max_channel:
                self.__channel = self.min_channel
            else:
                self.__channel += 1
            return self.__channel

    def channel_down(self) -> None:
        'Channel number should decrease unless it is the minimum'
        if self.__status:
            if self.__channel == self.min_channel:
                self.__channel = self.max_channel
            else:
                self.__channel -= 1
            return self.__channel

    def volume_up(self) -> None:
        'Volume should increase unless it is at max volume'
        if self.__status:
            if self.__muted == True:
                self.__volume = self.__volume
            if self.__volume == self.max_volume:
                self.__volume = self.max_volume
            else:
                self.__volume += 1
            return self.__volume

    def volume_down(self) -> None:
        'Volume should decrease unless it is at minimum volume'
        if self.__status:
            if self.__muted == True:
                self.__volume = self.__volume
            if self.__volume == self.min_volume:
                self.__volume = self.min_volume
            else:
                self.__volume -= 1
            return self.__volume

    def __str__(self) -> str:
        "Return the status, channel, and volume of the TV using a string"
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'







