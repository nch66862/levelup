from django.db import models


class Game(models.Model):

    name = models.CharField(max_length=50)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    max_players = models.IntegerField()
    min_players = models.IntegerField()
    difficulty = models.CharField(max_length=50)