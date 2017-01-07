#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

# Martin Kersner, m.kersner@gmail.com
# 2017/01/07

from bs4 import BeautifulSoup
from utils import *
from db import *

class Naver:
  search_url = "https://search.naver.com/search.naver?query={0}"
  category_dict = []
  db = sqliteDB()

  def __init__(self):
    self.category2searchTerm()

  def check_category(self, category):
    search_term = self.category_dict[category]

    url = self.search_url.format(search_term)
    html = requestPage(url)
    soup = BeautifulSoup(html, "html.parser")
    
    lst_realtime_srch = soup.find_all("ol", class_="lst_realtime_srch")[0]
    span = lst_realtime_srch.find_all("span")
    
    naver_dict = {}
    idx = 1
    for span_elem in span:
      if span_elem.get("class") != None and span_elem.get("class")[0] == "tit":
        naver_dict[idx] = span_elem.contents[0]
        print(idx, span_elem.contents[0])
        idx += 1

    self.db.AddToNaver(category, naver_dict)

  def category2searchTerm(self):
    self.category_dict = {"phone": "iphone",
                          "notebook": "macbook"}

n = Naver()
# phone, notebook
n.check_category("phone")
n.check_category("notebook")
