from urllib.parse import unquote, urlparse
from pathlib import Path
from datetime import datetime
import os
import requests


def download_img(url, file_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    os.makedirs("images")
    with open(file_path, 'wb') as file:
        file.write(response.content)
