from django.db import models
from clock import Clock
from clock import add_time, create_clock_from_str
import views
# Create your models here.

from django.contrib.auth.models import User

class Project(models.Model): 
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, unique=False)
    name = models.CharField(max_length=200, null=False)
    time = models.CharField(max_length=8, null=False, blank=False)
    idol = models.CharField(max_length=8, null=False, blank=False)
    clicks = models.IntegerField(null=False, blank=False)
    pressess = models.IntegerField(null=False, blank=False) 

    def __str__(self):
        return (f'{self.name}')
   
    @property
    def total_screens(self):
        screenshots = self.screenshot_set.all()  # type: ignore
        count = screenshots.count()
        return count

    @property
    def get_screenshot(self):
        screenshot = (self.screenshot_set.all()).first()  # type: ignore
        if screenshot:
            return str(screenshot.screenshot)
        else:
            return 'none'
    @property
    def get_screenshots(self):
        screens_list = []
        try:
            screenshots = self.screenshot_set.all() 
            for screenshot in screenshots:
                screens_list.append(str(screenshot.screenshot)) 
            return screens_list
        except:
            return screens_list

    @property
    def get_activity(self):
        time = create_clock_from_str(self.time)
        idol = create_clock_from_str(self.idol)
        work_time = add_time(time, idol)
        work_time = work_time.get_total_seconds()
        try:
            activity = (time.get_total_seconds()/work_time)*100
        except ZeroDivisionError:
            activity=0
        return round(activity)
    
    @property
    def get_worktime(self):
        if self.time:
            return self.time
        else:
            return '00:00:00'
        """if self.time:
            total_time = create_clock_from_str(self.time)
            if self.idol:
                idol = create_clock_from_str(self.idol)
            else:
                idol = create_clock_from_str('00:00:00') 
            work_time = subtract_time(total_time, idol)
            return work_time.get_time()
        return '00:00:00"""




class ScreenShot(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='',default='')
    

class UserSetting(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Screenshot_dalay = models.IntegerField(null=True)
    
    
class TimeSheet(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('View', 'View'),
        ('Submit', 'Submit'),
        ('Approve', 'Approve'),
        ('Deny', 'Deny'),
    )
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='Open')

class akbacbqg_trackify(models.Model):
    class Meta:
        db_table = 'akbacbqg_trackify',
        managed = False