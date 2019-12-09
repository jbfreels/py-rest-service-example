import json

class Index:
  urls = ()
  def __init__ (self):
    with open ("json/index.json", 'r') as f:
      self.data = f.read ()
      self.json = json.loads (self.data)
    self.urls = self.load_urls (self.json)

  def load_urls (self, json):
    urls = ()
    for url in json:
      urls = urls + (json[url]['pattern'], eval (json[url]['classname']))
    return urls
  
  def GET (self):
    return self.json

class GetTemplateList:
  def __init__ (self):
    with open ("json/GetTemplateList01.json", 'r') as f:
      self.data = f.read ()
      self.json = json.loads (self.data)

  def GET (self):
    return self.json