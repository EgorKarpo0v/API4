from urllib.parse import unquote, urlparse
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from launch import launch_img
import os
import requests



def get_earth_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    count = 5
    params = {
        "api_key":api_key,
        "count": count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_imgs = response.json()
    for img in epic_img:
        epic_name = img["image"]
        epic_date = img["date"]
        formatted_date = datetime.fromisoformat(epic_date).strftime("%Y/%m/%d")
        link = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{epic_name}.png"
        file_path = os.path.join("images", f"{epic_name}.png")
        download_img(link, file_path, params)
        

def main():
    load_dotenv()
    api_key = os.enivron["NASA_TOKEN"]
    get_earth_images(api_key)
    

if __name__ == "__main__":
    main()
