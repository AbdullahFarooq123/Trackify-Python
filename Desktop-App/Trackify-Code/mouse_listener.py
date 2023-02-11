import datetime

from pynput.mouse import *

import clock
from project import Project


class MouseInputs:
    def __init__(self):
        self.listener = None
        self.last_pressed_time = clock.create_clock_from_str(str(datetime.datetime.now().time()).split('.')[0])

    def mouse_clicked(self, project: Project, pressed: bool):
        if pressed:
            project.clicks += 1
            self.last_pressed_time = clock.create_clock_from_str(str(datetime.datetime.now().time()).split('.')[0])

    def add_listener(self, project: Project):
        self.listener = Listener(on_click=lambda x, y, button, pressed: self.mouse_clicked(project, pressed))
        self.listener.start()

    def remove_listener(self):
        self.listener.stop()
