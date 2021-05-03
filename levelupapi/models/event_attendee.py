from django.db import models

class EventAttendee(models.Model):

    gamer_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)