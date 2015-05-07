from xml.parsers.expat import ExpatError
from xml.dom.minidom import parseString, getDOMImplementation
from entitygateway.factory_smile_entitygateway import EnergyMeterGatewayFactory

class SmileEntityGatewayException(Exception):
   def __init__(self, value):
      self.value = value

   def __str__(self):
      return repr(self.value)

class SmileEntityGateway(object):
   def __init__(self):
      self.smileXMLData = None
      self.energyMeterFactory = EnergyMeterGatewayFactory() 
   
   def getEnergyMeters(self):
      if self.smileXMLData == None:
         self.smileXMLData = "" # TODO ophalen
      smileDom = self._getDom(self.smileXMLData)
      smileModules = smileDom.getElementsByTagName('module')
      meters = []
      for moduleDom in smileModules:
         moduleDoc = getDOMImplementation().createDocument(None, None, None)
         moduleDoc.appendChild(moduleDom)
         energyMeterGateway = self.energyMeterFactory.getEnergyMeterGateway(moduleDoc)
         energyMeter = energyMeterGateway.getEnergyMeter()
         meters.append(energyMeter)
      return meters      
   
   def _getDom(self, xmlString):
      try:
         dom = parseString(xmlString)
      except ExpatError, ea:
         raise SmileEntityGatewayException(ea)
      return dom

