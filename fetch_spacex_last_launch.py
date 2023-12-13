
from pathlib import Path
import os
import requests
from launch import launch_img
import argparse


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    spacex_imgs = response.json()["links"]["flickr"]["original"]
    for img_number, img in enumerate(spacex_imgs):
        file_name = f"spacex_{img_number}.jpeg"
        path = os.path.join("images", file_name)
        launch_img(img, path)


def main():
    fetch_spacex_last_launch()
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--id', help='Напишите id запуска SpaceX', default = "5eb87d47ffd86e000604b38a")


if __name__ == "__main__":
    main()
