import pandas as pd
import requests
from bs4 import BeautifulSoup

# specify mtn project user id and build url
user_id = 200544978
url = f"https://www.mountainproject.com/user/{user_id}"

# get page html
profile = requests.get(url)
soup = BeautifulSoup(profile.content, "html.parser")
print(soup.find_all("script"))