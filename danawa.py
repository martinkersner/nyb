#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

# Martin Kersner, m.kersner@gmail.com
# 2016/12/27

from bs4 import BeautifulSoup
from utils import *
from db import *

class Danawa:
  search_url100 = "http://www.danawa.com/Keyword/keyword_ranking.html"
  search_url10  = "http://search.danawa.com/dsearch.php?k1={0}"
  db = sqliteDB()

  def Get100(self):
    html = requestPage(self.search_url100)
    soup = BeautifulSoup(html, "html.parser")
    
    week_rank_wrap = soup.find_all("div", class_="week_rank_wrap")[0]
    keyword = week_rank_wrap.find_all("a")
    
    danawa_dict = {}
    for idx, keyword in enumerate(keyword):
        danawa_dict[idx+1] = keyword.contents[1]
        print(idx+1, keyword.contents[1])
    
    self.db.AddToDanawa100(danawa_dict)

  def Get10(self):
    html = requestPage(self.search_url10.format(""))
    soup = BeautifulSoup(html, "html.parser")

    ranking_wrap = soup.find_all("div", class_="ranking_wrap")[0]
    keyword_link = ranking_wrap.find_all("a")
    
    danawa_dict = {}
    for idx, keyword in enumerate(keyword_link):
        danawa_dict[idx+1] = keyword.contents[0]
        print(idx+1, keyword.contents[0])
    
    self.db.AddToDanawa10(danawa_dict)
    

danawa = Danawa()
danawa.Get100()
danawa.Get10()
