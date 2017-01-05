#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

# Martin Kersner, m.kersner@gmail.com
# 2016/12/27

from bs4 import BeautifulSoup
import urllib.request as urlrequest
import urllib.error as urlerror
from db import *

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

url = "http://www.danawa.com/Keyword/keyword_ranking.html"

request_obj = urlrequest.Request(
        url=url,
        method="GET",
        headers={"User-agent": "hey"})

html = requestPage(request_obj)
soup = BeautifulSoup(html, "html.parser")

week_rank_wrap = soup.find_all("div", class_="week_rank_wrap")[0]
keyword = week_rank_wrap.find_all("a")

dict_danawa = {}
for idx, keyword in enumerate(keyword):
    dict_danawa[idx+1] = keyword.contents[1]
    print(idx+1, keyword.contents[1])

db = sqliteDB()
db.AddToDanawa100(dict_danawa)
