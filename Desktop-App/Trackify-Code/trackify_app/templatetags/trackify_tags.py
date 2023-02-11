from ..models import Project
from django import template
from ..views import *
from clock import *

register = template.Library()
from ..models import Project
from django import template

register = template.Library()

@register.simple_tag
def get_project(user):
    try:
        project = Project.objects.get(user=user)
    except:
        return ""
    return project.name

@register.simple_tag
def get_project_activity(user):
    try:
        project = Project.objects.get(user=user)
    except:
        return ""
    return getActivity(create_clock_from_str(project.time),create_clock_from_str(project.idol))

@register.simple_tag
def get_project_time(user):
    try:
        project = Project.objects.get(user=user)
    except:
        return ""
    return project.time

@register.simple_tag
def get_screenshot(project):
    try:
        screenshots = project.screenshot_set.all()  # type: ignore
        return screenshots[0].screenshot
    except:
        return 'none'