import time

from project import Project


class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.exit = False

    def get_time(self):
        return f'{"{:02d}".format(self.hours)}:{"{:02d}".format(self.minutes)}:{"{:02d}".format(self.seconds)}'

    def get_total_seconds(self):
        return self.hours * 60 * 60 + self.minutes * 60 + self.seconds


def subtract_time(time_1: Clock, time_2: Clock):
    time_1_seconds = time_1.get_total_seconds()
    time_2_seconds = time_2.get_total_seconds()
    seconds_difference = abs(time_1_seconds - time_2_seconds)
    return seconds_to_clock(seconds_difference)


def seconds_to_clock(seconds: int):
    hours = seconds / 3600
    minutes = (hours % 1) * 60
    seconds = round((minutes % 1) * 60)
    if seconds >= 60:
        seconds = 0
        minutes += 1
        if minutes >= 60:
            minutes = 0
            hours += 1
    return Clock(hours=int(hours), minutes=int(minutes), seconds=seconds)


def add_time(time_1: Clock, time_2: Clock):
    time_1_seconds = time_1.get_total_seconds()
    time_2_seconds = time_2.get_total_seconds()
    seconds_difference = time_1_seconds + time_2_seconds
    return seconds_to_clock(seconds_difference)


def create_clock_from_str(time_str: str):
    separates = time_str.split(':')
    hours = int(separates[0])
    minutes = int(separates[1]) % 60
    seconds = int(separates[2]) % 60
    return Clock(hours=hours, minutes=minutes, seconds=seconds)
