from entity.energymeter import EnergyMeter

class ElectricityMeter(EnergyMeter):
  def __init__(self, debug=False):
    super(ElectricityMeter, self).__init__(debug)
    self.vendor_name = ""
    self.vendor_model = ""
      
  def __eq__(self, other):
    if super(ElectricityMeter, self).__eq__(other) and\
       self._isEqual(self.vendor_name, other.vendor_name) and\
       self._isEqual(self.vendor_model, other.vendor_model):
      return True
    else:
      return False
   
  def __str__(self):
    return "vendor: " + self.vendor_name + "\nmodel: " + self.vendor_model + "\n" + \
            super(ElectricityMeter, self).__str__()
