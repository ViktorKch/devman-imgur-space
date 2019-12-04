import requests
import pathlib
import os
from imgurpython import ImgurClient
from dotenv import load_dotenv
from os import listdir
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import save_hubble_image


def authenticate():
	
	client = ImgurClient(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

	authorization_url = client.get_auth_url('pin')

	print("Go to the following URL: {0}".format(authorization_url))

	pin = input("Enter pin code: ")

	credentials = client.authorize(pin, 'pin')
	client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

	print("Authentication successful! Here are the details:")
	print("   Access token:  {0}".format(credentials['access_token']))
	print("   Refresh token: {0}".format(credentials['refresh_token']))

	return client

def upload_image(client, image_name):

  image = client.upload_from_path('images/{}'.format(image_name))

  return image

if __name__ == "__main__":

    load_dotenv()
    fetch_spacex_last_launch()

    response = requests.get("http://hubblesite.org/api/v3/images?page=all&collection_name=stsci_gallery")
    ids = []
    for picture in response.json():
        ids.append(picture['id'])

    for id in ids:
        save_hubble_image(id)

    client = authenticate()
    images = listdir('images')
    for image_name in images:
        image = upload_image(client, image_name)
        
    

