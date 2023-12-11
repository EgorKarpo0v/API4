from urllib.parse import unquote, urlparse
from pathlib import Path
from launch import launch_img
import os
import requests


def get_APOD_img():
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": "7BYLApy7LKcz3stq03ImiatyG0srY3D629q6rSmE",
        "count": 5
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    for img in response.json():
        if img.get("media_type") == "image":
            if img.get("hdurl"):
                nasa_img = img["hdurl"]
            else:
                nasa_img = img["url"]
        extention_file, file_name = get_file_format(nasa_img)
        file_path = os.path.join("images", f"{file_name}{extention_file}")
        launch_img(nasa_img, file_path)


def get_file_format(url):
    decoded_url = unquote(url)
    parsed_url = urlparse(decoded_url)
    file_path, fullname = os.path.split(parsed_url.path)
    extention = os.path.splitext(fullname)
    file_name, extention_file = extention
    return extention_file, file_name
def main():
    get_APOD_img()
    get_file_format(url)
if __name__ == "__main__":
    main()