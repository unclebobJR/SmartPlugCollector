class XMLHelperException(Exception):
  def __init__(self, value):
    self.value = value
  
  def __str__(self):
    return repr(self.value)

class XML_helper(object):
  def __init__(self, dom):
    self.dom = dom
  
  def getListFromTagName(self, tagName):
    return self.dom.getElementsByTagName(tagName)
  
  def _getElementListFromTagName(self, tagName):
    elementList = self.dom.getElementsByTagName(tagName)
    if len(elementList) != 1:
      raise XMLHelperException("Wrong number of elements (" + \
                              str(len(elementList)) + ") of " + tagName + " in xml:\n" + \
                              self.dom.toxml())
    return elementList

  def _getAttributeFromTagName(self, tagName, attributeName):
    elementList = self._getElementListFromTagName(tagName)
    attr_value = elementList[0].getAttribute(attributeName)
    if attr_value == None or attr_value == "":
      return ""
    else:
      return attr_value

  def _getTextFromTagName(self, tagName):
    elementList = self._getElementListFromTagName(tagName)
    return elementList[0].firstChild.data      
  
  def prettyPrint(self):
    print self.dom.toxml()
