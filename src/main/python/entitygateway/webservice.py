import requests
class WebServiceException(Exception):
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)

class WebService(object):
  def __init__(self):
    self.url = None
    self.userID = None
    self.password = None
    self.requests = requests()
    
  def getContent(self):
    raise WebServiceException("fail for: " + self.url)