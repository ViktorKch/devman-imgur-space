import requests
import os
import pathlib

BASE_URL = 'https://api.spacexdata.com/v3/launches/latest'

def save_image(image_url, picture_name):
  
  response = requests.get(image_url, verify=False)

  with open(os.path.join("images", picture_name), 'wb') as file:
    file.write(response.content)


def fetch_spacex_last_launch():

  response = requests.get(BASE_URL)
  response.raise_for_status()
  images_url = response.json()['links']['flickr_images']

  if not images_url:
        raise requests.exceptions.HTTPError('Нет фотографий последнего запуска.')

  for image_number, image_url in enumerate(images_url):
    save_image(image_url, 'spacex{}.jpg'.format(image_number + 1))
