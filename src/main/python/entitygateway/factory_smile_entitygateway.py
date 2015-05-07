from entitygateway.xml_helper import XML_helper, XMLHelperException
from entitygateway.smile_energymetergateway import GasMeterGateway, ElectricityMeterGateway

class EnergyMeterGatewayFactoryException(Exception):
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)

     
class EnergyMeterGatewayFactory(object):
  def __init__(self):
    pass
     
  def getEnergyMeterGateway(self, xmlModuleDom):
    if self._isModuleForGas(xmlModuleDom):
      return GasMeterGateway(xmlModuleDom)
    elif self._isModuleForElectricity(xmlModuleDom):
      return ElectricityMeterGateway(xmlModuleDom)
    else:
      raise EnergyMeterGatewayFactoryException("xml is of unknown type: Must be electricity of gas")
  
  def _isModuleForGas(self, moduleDom):
    return self._isTypeOf(moduleDom, 'gas')
  
  def _isModuleForElectricity(self, moduleDom):
    try:
      log = moduleDom.getElementsByTagName('cumulative_log')
    except XMLHelperException:
      return False
    if len(log) == 0:
      raise EnergyMeterGatewayFactoryException("Invalid Module: No cumulative_log")
    return self._isTypeOf(log[0], 'electricity')
  
  def _isTypeOf(self, dom, _type):
    try:
      xmlHelper = XML_helper(dom)         
      moduleType = xmlHelper._getTextFromTagName('type')
    except XMLHelperException:
      return False
    if _type in moduleType:
      return True
    else:
      return False
