from django.db import models

class EventAttendee(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey("Event", on_delete=models.SET_NULL, null=True)