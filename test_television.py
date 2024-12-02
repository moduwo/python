import pytest
from television import *



class Test:
    def setup_method(self):
        self.tv = Television()
    def teardown_method(self):
        del self.tv
    def test__init__(self):
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv.power()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv.power()
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.channel_down()
        assert self.tv__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        self.tv.power()
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tv.power()
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power == False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__ == 'Power = True, Channel = 0, Volume = 1'
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
