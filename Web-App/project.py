


class Project:
    def __init__(self, scrollAreaWidgetContents, project_name: str, project_time: str, project_idol_time: str,
                 screen_shots: list, clicks: int, presses: int):
        self.project_name = project_name
        self.project_time = project_time
        self.project_idol_time = project_idol_time
        self.screen_shots = screen_shots
        self.clicks = clicks
        self.presses = presses
