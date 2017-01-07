#-*- encoding: utf-8 -*-

# Martin Kersner, m.kersner@gmail.com
# 2017/01/07

import urllib.request as urlrequest
import urllib.error as urlerror

def requestPage(url):
  request_obj = makeRequestObject(url)

  try:
    response = urlrequest.urlopen(request_obj)
  except urlerror.URLError as err:
    print("Hit URLError", err.msg)
    exit(-1)
  except urlerror.HTTPError as err:
    print("Hit HTTPError", err.code, "-", err.msg)
    exit(-1)
  
  return response.read()

def makeRequestObject(url):
  return urlrequest.Request(url=url,
                            method="GET",
                            headers={"User-agent": "hey"})
