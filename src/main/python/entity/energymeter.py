
class EnergyMeter(object):
  def __init__(self, debug=False):
    self.id = ""
    self.debug = debug
    self.logs = set()
     
  def __eq__(self, other):
    if self._isEqual(self.id, other.id) and\
      self._isEqualSets(self.logs, other.logs):
      return True
    else:
      return False
  
  def _isEqual(self, one, other):
    if one == other:
      return True
    else:
      if self.debug:
        print str(one) + " != " + str(other)
      return False
     
  def _isEqualSets(self, aSet, otherSet):
    for el in aSet:
      for elOther in otherSet:
        if el == elOther:
          otherSet.remove(elOther)
          break
    if len(otherSet) == 0:
      return True
    else:
      return False
     
  def __str__(self):
    logString = ""
    for log in self.logs:
      logString = logString + str(log)
    return "id: " + self.id + logString
