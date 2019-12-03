from django.db import models
from modelchoices import Choices


class Anime(models.Model):
    
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=20)
    thumbnail_url = models.URLField(max_length = 2500, default="")
    image_url = models.URLField(max_length = 2500, default="")

    def __str__(self):

        episodes = self.episode_set.all()
        episodes_info = ''
        for ep in episodes:
            episodes_info += (str(ep)+'\n')
        return "Title: {} | Status: {}\n    {}".format(self.title, self.status, episodes_info)
    

class Episode(models.Model):
    number = models.IntegerField()
    volume = models.IntegerField()
    from_chapter = models.IntegerField()
    to_chapter = models.IntegerField()

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return "Episode N°: {} -> From: Ch.{} To: Ch.{} In: Vol.{}".format(self.number, self.from_chapter, self.to_chapter, self.volume)


