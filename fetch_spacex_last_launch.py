
from pathlib import Path
import os
import requests
from launch import launch_img
import argparse


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    spacex_imgs = response.json()["links"]["flickr"]["original"]
    for img_number, img in enumerate(spacex_imgs):
        file_name = f"spacex_{img_number}.jpeg"
        path = os.path.join("images", file_name)
        download_img(img, path)


def main():
    parser = argparse.ArgumentParser(
        description='Програма позволяет получать фотографии запуска SpaceX'
    )
    parser.add_argument('--id', dest="launch_id", help='Напишите id запуска SpaceX', default = "5eb87d47ffd86e000604b38a")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == "__main__":
    main()
