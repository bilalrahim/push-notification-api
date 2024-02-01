from django.db import models

class Notification(models.Model):
    message = models.TextField()

    class Meta:
        app_label = 'notifications'
