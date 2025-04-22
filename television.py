class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Default values for tv.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Toggles power on or off.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Toggles mute or unmute.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increases volume by one if current channel is less than max channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Decreases volume by one if current channel is greater than max channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Increases volume by one if current volume is less than max volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Decreases volume by one if current volume is greater than max volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        A string to display current status of tv objects Power, Channel, and Volume.
        """
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"
