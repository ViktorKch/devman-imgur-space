import requests
import os
import pathlib

BASE_URL = 'http://hubblesite.org/api/v3/image/{}'

def save_image(image_url, picture_name):
  
  response = requests.get(image_url, verify=False)

  with open(os.path.join("images", picture_name), 'wb') as file:
    file.write(response.content)

def save_hubble_image(image_id):
  url = BASE_URL.format(image_id)
  response =  requests.get(url)
  response.raise_for_status()
  images = response.json()['image_files']

  if not images:
        raise requests.exceptions.HTTPError('Фотографии с заданным id не существует.')

  image_url = 'http:{}'.format(images[-1]['file_url'])
  extension = os.path.splitext(image_url)[-1]
  save_image(image_url, 'hubble{}{}'.format(image_id, extension))

