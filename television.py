class Television:
    min_volume:int = 0
    max_volume:int = 2
    min_channel:int = 0
    max_channel:int = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True
        return self.__status

    def mute(self):
        if self.__muted:
            self.__muted = True
        if self.__muted:
            self.__volume = self.min_volume
        return self.__volume

    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > self.max_channel:
                self.__channel = self.min_channel
            return self.__channel

    def channel_down(self):
        if self.__status:
            if self.__channel == self.min_channel:
                return self.__channel
            else:
                self.__channel -= 1
                return self.__channel

    def volume_up(self):
        if self.__status:
            if self.__volume == self.max_volume:
                return self.__volume
            else:
                self.__volume += 1
                return self.__volume

    def volume_down(self):
        if self.__status:
            if self.__volume == self.min_volume:
                return self.__volume
            else:
                self.__volume -= 1
                return self.__volume

    def __str__(self):
        return f'Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}'







