import os

import ftpretty

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trackify_database.settings")
import django

django.setup()
from .models import Project, ScreenShot, UserSetting
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def sign_in(username, password):
    return authenticate(username=username, password=password) is not None


def get_projects(username):  # this method returns user, user settings and all the projects of that user
    object = {}
    try:
        user = User.objects.get(username=username)
        try:
            projects = Project.objects.filter(user=user)
            user_projects = []
            for project in projects:
                user_projects.append(
                    {
                        "project name": project.name,
                        "project time": project.time,
                        "project idol": project.idol,
                        "project screenshots": [],
                        "project clicks": project.clicks,
                        "project presses": project.pressess
                    }
                )
            object.update({"projects": user_projects})
        except Project.DoesNotExist:
            object.update({"projects": list()})
            # projects contain list of projects
        try:
            user_setting = UserSetting.objects.get(user=user)
            object.update({'settings': user_setting.Screenshot_dalay})  # type: ignore
        except UserSetting.DoesNotExist:
            object.update({"settings": {"screenshot delay": 5}})

    except User.DoesNotExist:
        print("The user does not exist")
    return object


def update_project(username, project):
    try:
        user = User.objects.get(username=username)
        try:
            project_obj = Project.objects.get(name=project.project_name)
            project_obj.name = project.project_name
            project_obj.time = project.project_time
            project_obj.idol = project.project_idol_time
            project_obj.clicks = project.clicks
            project_obj.pressess = project.presses
            project_obj.save()

            screenshots = project_obj.screenshot_set.all()  # type: ignore

            for screenshot in screenshots:
                screenshot.delete()

            for screenshot in project.screen_shots:
                ScreenShot.objects.create(
                    project=project_obj,
                    screenshot=screenshot.replace("screen shots/", '')
                )
            put_screenshots(project.screen_shots)

        except Project.DoesNotExist:
            project_obj = Project(
                user=user,
                name=project.project_name,
                time=project.project_time,
                idol=project.project_idol_time,
                clicks=project.clicks,
                pressess=project.presses,
            )
            project_obj.save()

            for screenshot in project.screen_shots:
                ScreenShot.objects.create(
                    project=project_obj,
                    screenshot=screenshot,
                )

    except User.DoesNotExist:
        print("The user does not exist")


def put_screenshots(screenshots: str):
    ftp = ftpretty.ftpretty(host='162.0.217.84', user='akbacbqg', password='RfCf67!344d%F2c7')
    for screenshot in screenshots:
        ftp.put(screenshot, '/trackify.onweb.host/static/screenshots/' + screenshot.replace("screen shots/", ''))
    ftp.close()
