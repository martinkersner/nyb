#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

# Martin Kersner, m.kersner@gmail.com
# 2016/12/24

from bs4 import BeautifulSoup
import urllib.request as urlrequest
import urllib.error as urlerror
from utils import getRandomString

# html_file = 'danawa.html'
# with open(html_file, encoding="utf-8") as f:

def requestPage(request_obj):
    try:
        response = urlrequest.urlopen(request_obj)
    except urlerror.URLError as err:
        print("Hit URLError", err.msg)
        exit(-1)
    except urlerror.HTTPError as err:
        print("Hit HTTPError", err.code, "-", err.msg)
        exit(-1)
    
    return response.read()

# rand_str = getRandomString()
rand_str = ""
url = "http://search.danawa.com/dsearch.php?k1={0}".format(rand_str)

request_obj = urlrequest.Request(
        url=url,
        method="GET",
        headers={"User-agent": "hey"})

html = requestPage(request_obj)
soup = BeautifulSoup(html, "html.parser")

ranking_wrap = soup.find_all("div", class_="ranking_wrap")[0]
keyword_link = ranking_wrap.find_all("a")

for idx, keyword in enumerate(keyword_link):
    print(idx, keyword.contents[0])
