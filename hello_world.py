import pandas as pd
import requests
from bs4 import BeautifulSoup

# specify mtn project user id and build url
user_id = 200544978
url = f"https://www.mountainproject.com/user/{user_id}"
print(url)
