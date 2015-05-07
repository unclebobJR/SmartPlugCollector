class EnergyLog(object):
  def __init__(self, last_consecutive_date="", start_date="", end_date="", \
               measurement_date="", measurement=0.0, unit="", _type="", \
               usage="", tariff="", debug=False):
    self.last_consecutive_date = last_consecutive_date
    self.start_date = start_date
    self.end_date = end_date
    self.measurement_date = measurement_date
    self.measurement = measurement
    self.unit = unit
    self.type = _type
    self.tariff = tariff
    self.usage = usage
    self.debug = debug

  def isConsumed(self):
    if 'consumed' in self.usage:
      return True
    else:
      return False
     
  def isOffPeak(self):
    if self.tariff == 'nl_offpeak':
      return True
    else:
      return False
  
  def __eq__(self, other):
    if self._isEqual(self.start_date, other.start_date) and\
      self._isEqual(self.end_date, other.end_date) and\
      self._isEqual(self.last_consecutive_date, other.last_consecutive_date) and\
      self._isEqual(self.measurement_date, other.measurement_date) and\
      self._isEqual(self.unit, other.unit) and\
      self._isEqual(self.type, other.type) and\
      self._isEqual(self.tariff, other.tariff) and\
      self._isEqual(self.usage, other.usage) and\
      self._isEqual(self.measurement, other.measurement):
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
     
  def __str__(self):
    out = ""
    out = out + "\ntariff    : " + str(self.tariff)
    out = out + "\ntype      : " + str(self.type)
    out = out + "\nusage     : " + str(self.usage)      
    out = out + "\nlast Date : " + str(self.last_consecutive_date)
    out = out + "\nstart Date: " + str(self.start_date)
    out = out + "\nend Date  : " + str(self.end_date)
    out = out + "\nmeas Date : " + str(self.measurement_date)
    out = out + "\nmeas val  : " + str(self.measurement)
    out = out + "\nunit      : " + str(self.unit)
    out = out + "\n------------"
    return out
