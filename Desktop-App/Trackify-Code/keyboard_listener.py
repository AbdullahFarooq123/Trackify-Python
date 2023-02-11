import datetime

from pynput.keyboard import *

import clock
from project import Project


class KeyboardInputs:
    def __init__(self):
        self.listener = None
        self.last_pressed_time = clock.create_clock_from_str(str(datetime.datetime.now().time()).split('.')[0])

    def press_off(self, project: Project):
        project.presses += 1
        self.last_pressed_time = clock.create_clock_from_str(str(datetime.datetime.now().time()).split('.')[0])

    def add_listener(self, project: Project):
        self.listener = Listener(on_press=lambda key: self.press_off(project))
        self.listener.start()

    def remove_listener(self):
        self.listener.stop()
