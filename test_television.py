import pytest
from television import *


class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power()  # TV on
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.power()  # TV off
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        # The tv details when the tv is on, volume increased once, and then tv muted.
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # The tv details when the tv is on and unmuted.
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # The tv details when the tv is off and muted.
        self.tv1.power()  # turn OFF
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1'

        # The tv details when the tv is off and unmuted.
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        # The tv details when the tv is off and the channel has been increased.
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #The tv details when the tv is on and the channel has been increased.
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'

        # The tv details when the tv is on and one has increased the channel past the maximum value
        self.tv1.channel_up()  # Changes channel to 2.
        self.tv1.channel_up()  # Changes channel to 3.
        self.tv1.channel_up()  # Changes channel to 0.
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        # The tv details when the tv is off and the channel has been decreased.
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # The tv details when the tv is on and one has decreased the channel past the minimum value
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        # The tv details when the tv is off and the volume has been increased
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # The tv details when the tv is on and the volume has been increased
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # The tv details when the tv is on, muted, and the volume has been increased.
        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        # The tv details when the tv is on and one has increased the volume past the maximum value.
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        # The tv details when the tv is off and the volume has been decreased.
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # The tv details when the tv is on and the volume has been decreased (increase the volume to the maximum before decreasing to see the decreasing effect).
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # The tv details when the tv is on, muted, and the volume has been decreased.
        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # The tv details when the tv is on and one has decreased the volume past the minimum value.
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
