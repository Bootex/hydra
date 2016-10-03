from django.db import models
from django.utils import timezone


# Create your models here.
class Todolist(models.Model):
    task_name = models.CharField(max_length=100)
    task_detail = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

    def __str__(self):
        return self.task_name


class Login(models.Model):
    user = models.ForeignKey('auth.User')
    password = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    recent_login = models.DateTimeField(default=timezone.now)

    def login_check(self):
        self.recent_login = timezone.now
        self.save()

    def __str__(self):
        return self.user