from urllib.parse import unquote, urlparse
from pathlib import Path
from datetime import datetime
import os
import requests
from launch import launch_img


def get_Earth_image():
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        "api_key":"7BYLApy7LKcz3stq03ImiatyG0srY3D629q6rSmE",
        "count": 5
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_img = response.json()
    for img in epic_img:
        epic_name = img["image"]
        epic_date = img["date"]
        formatted_date = datetime.fromisoformat(epic_date).strftime("%Y/%m/%d")
        link = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{epic_name}.png"
        file_path = os.path.join("images", f"{epic_name}.png")
        launch_img(link, file_path, params)
        print(epic_name)
        print(formatted_date)


def main():
    get_Earth_image()


if __name__ == "__main__":
    main()
