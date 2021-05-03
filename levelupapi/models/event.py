from django.db import models

class Event(models.Model):

    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    event_time = models.models.DateTimeField(_("what"), auto_now=False, auto_now_add=False)