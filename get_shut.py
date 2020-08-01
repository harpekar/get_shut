#!/usr/bin/python3 

from bs4 import BeautifulSoup
from PIL import Image 
from imageio import imread

import requests
import sys

search_term = "+".join(sys.argv[1:])

url = 'http://www.shutterstock.com/search/' + search_term

page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'})

#Get the link for the first resulting image 
try: img_url = BeautifulSoup(page.content, "html.parser").find("img").get('src')

except: print("No image results for that search")

else:
    img = Image.fromarray(imread(img_url))
    img.show()
