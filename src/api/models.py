from django.db import models
from modelchoices import Choices


class AnimeStatus(Choices):
    FINISHED = ('F', 'Finished')
    CURRENTLY = ('C', 'Currently')

class Anime(models.Model):
    
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=1, choices=AnimeStatus.CHOICES)

class Episode(models.Model):
    number = models.IntegerField()
    volume = models.IntegerField()
    from_chapter = models.IntegerField()
    to_chapter = models.IntegerField()

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)


