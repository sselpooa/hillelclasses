from django.db import models


class Task(models.Model):
    OPEN_STATUS = "open"
    TASK_STATUSES = (
        (OPEN_STATUS,'Open'),
        ('in_progress','In progress'),
        ('done','Done')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_lenghth=40)
    description = models.TextField()
    status = models.CharField(
        max_lenghth=40,
        choices=TASK_STATUSES,
        default=OPEN_STATUS
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)