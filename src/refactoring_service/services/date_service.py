import datetime


class DateService:
    @property
    def today(self):
        return datetime.datetime.now().weekday()

    def is_today_weekend(self):
        """

        :return: True for Saturday and Sunday
        """
        return self.today > 4

    def is_today_magic_day(self):
        """

        :return: True if today weekday number modulus 2 equals 0 else False
        """
        return self.today % 2 == 0
