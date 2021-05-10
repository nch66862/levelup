from django.db import models

class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='events')
    event_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='the_host')
    attendees = models.ManyToManyField("Gamer", through="EventAttendee", related_name="attending")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

    @property
    def number_of_attendees(self):
        return self.__number_of_attendees

    @number_of_attendees.setter
    def number_of_attendees(self, value):
        self.__number_of_attendees = value