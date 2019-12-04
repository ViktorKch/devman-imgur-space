import requests
import os
import pathlib

BASE_URL = 'http://hubblesite.org/api/v3/image/{}'
pathlib.Path('images').mkdir(parents=True, exist_ok=True)

def save_image(image_url, picture_name):
  
  response = requests.get(image_url, verify=False)

  with open(os.path.join("images", picture_name), 'wb') as file:
    file.write(response.content)

def get_extension(url):
  return url.split('.')[-1]

def save_hubble_image(image_id):
  url = BASE_URL.format(image_id)
  response =  requests.get(url)
  images = response.json()['image_files']
  image_url = 'http:{}'.format(images[-1]['file_url'])
  extension = get_extension(image_url)
  save_image(image_url, 'hubble{}.{}'.format(image_id, extension))

