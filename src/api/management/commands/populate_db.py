from django.core.management.base import BaseCommand, CommandError
from api.models import Anime, Episode

import requests
import json


class Command(BaseCommand):
    help = 'Populate db with the data extracted from anime-json-db github repo.'

    def add_arguments(self, parser):
        return super().add_arguments(parser)

    def handle(self, *args, **kwargs):
        # Get the data from github
        url = "https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json"
        print("Downloading database from github.")
        response = requests.get(url)

        # Parse the data and extract the needed informations
        json_data = json.loads(response.content)
        
        prev_anime = {'title': ''}

        parsed_data = []

        for anime in json_data['data']:
            if int(anime['episodes']) != 0 and anime["status"] != "UPCOMING" and anime["title"].lower() != prev_anime["title"].lower() and anime["type"] == "TV":

                for source in anime["sources"]:
                    if "https://myanimelist.net/" in source:
                        del anime['sources']
                        del anime['relations']
                        parsed_data.append(anime)

            prev_anime = anime
        
        for anime in parsed_data:
            anime_object = Anime.objects.create(title=anime['title'], status=anime['status'], image_url=anime['picture'], thumbnail_url=anime['thumbnail'])
            anime_object.save()

            number_of_episodes = int(anime['episodes'])
            for i in range(0, number_of_episodes):
                episode_object = Episode.objects.create(number=i+1, volume=0, from_chapter=0, to_chapter=0, anime=anime_object)
                episode_object.save()
            
            print(str(anime_object))
