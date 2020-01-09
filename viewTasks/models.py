from django.db import models

# Create your models here.


class TaskItem(models.Model):
    title = models.TextField(max_length=100, default='title', null=True)
    comment = models.TextField(max_length=240, default='comment', null=True)
    due_date = models.DateField(default='2020-01-01', null=True)
    star = models.BooleanField(null=True)


def __str__(self):
    return self.title + '-' + due_date
