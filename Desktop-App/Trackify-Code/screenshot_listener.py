import datetime
import os
import time

import pyautogui

from project import Project


class Screenshot:
    def __init__(self, delay_time: float):
        os.makedirs('screen shots', exist_ok=True)
        self.delay = delay_time
        self.stop_listening = False

    def _take_screen_shot(self, selected_project: Project):
        screen_shot = pyautogui.screenshot()
        selected_project.screen_shots.append(
            f'screen shots/{str(datetime.datetime.now()).split(".")[0].replace(":", ".")}.png')
        screen_shot.save(f'screen shots/{str(datetime.datetime.now()).split(".")[0].replace(":", ".")}.png')
        time.sleep(self.delay)

    def reset(self):
        self.stop_listening = False

    def add_listener(self, selected_project: Project):
        while not self.stop_listening:
            self._take_screen_shot(selected_project)

    def pause_listener(self):
        self.remove_listener()

    def resume_listener(self):
        self.reset()
        return self.add_listener

    def remove_listener(self):
        self.stop_listening = True
