from django.db import models


class Game(models.Model):

    name = models.CharField(max_length=50)
    game_type_id = models.ForeignKey(GameType, on_delete=models.CASCADE)