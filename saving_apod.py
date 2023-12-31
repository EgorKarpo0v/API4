from urllib.parse import unquote, urlparse
from pathlib import Path
from launch import launch_img
from dotenv import load_dotenv
import os
import requests

def get_file_format(url):
    decoded_url = unquote(url)
    parsed_url = urlparse(decoded_url)
    file_path, fullname = os.path.split(parsed_url.path)
    extention = os.path.splitext(fullname)
    file_name, extention_file = extention
    return extention_file, file_name
    
def get_space_imgs(api_key):
    url = "https://api.nasa.gov/planetary/apod"
    count = 5
    params = {
        "api_key": api_key,
        "count": count
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
        download_img(nasa_img, file_path)


def main():
    load_dotenv()
    api_key = os.enivron["NASA_API_KEY"]
    get_space_imgы(api_key)
    
    
if __name__ == "__main__":
    main()
