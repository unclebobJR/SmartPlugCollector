from entity.energy_log import EnergyLog
from entitygateway.xml_helper import XML_helper, XMLHelperException
from entity.gasmeter import GasMeter
from entity.electricitymeter import ElectricityMeter
class EnergyMeterGateway(object):
   def __init__(self, dom):
      self.smileDom = dom
      self.energyMeter = None
         
   def _getLog(self, xmlHelper, _type):
      log =  EnergyLog()
      log.start_date = xmlHelper._getAttributeFromTagName('period', 'start_date')
      log.end_date = xmlHelper._getAttributeFromTagName('period', 'end_date')
      log.last_consecutive_date = xmlHelper._getTextFromTagName('last_consecutive_log_date')
      log.measurement_date = xmlHelper._getAttributeFromTagName('measurement', 'log_date')
      log.measurement = float(xmlHelper._getTextFromTagName('measurement'))
      usage = xmlHelper._getTextFromTagName('type').split('_')
      log.usage = usage[1]
      log.unit = xmlHelper._getTextFromTagName('unit')
      log.tariff = xmlHelper._getAttributeFromTagName('measurement', 'tariff_type')
      log.type = _type
      return log

   def _setLogs(self, cumulativeLogDoms, _type):
      for logDom in cumulativeLogDoms:
         log = self._getLog(XML_helper(logDom), _type)
         self.energyMeter.logs.add(log)

   def _getEnergyMeterValues(self):
      self.xmlHelper = XML_helper(self.smileDom)
      self.energyMeter.id = self.xmlHelper._getAttributeFromTagName('module', 'id') 
      self._setLogs(self.smileDom.getElementsByTagName('cumulative_log'), "meterreading")
      self._setLogs(self.smileDom.getElementsByTagName('point_log'), "currentvalue")


class GasMeterGateway(EnergyMeterGateway):
   def __init__(self, smileDom):
      super(GasMeterGateway, self).__init__(smileDom)
      self.energyMeter = None 

   def getEnergyMeter(self):
      self.energyMeter = GasMeter()
      self._getEnergyMeterValues()
      return self.energyMeter
         
class ElectricityMeterGateway(EnergyMeterGateway):
   def __init__(self, smileDom):
      super(ElectricityMeterGateway, self).__init__(smileDom)
      self.energyMeter = None
      
   def getEnergyMeter(self):
      self.energyMeter = ElectricityMeter()
      self._getEnergyMeterValues()
      try:
         self.energyMeter.vendor_name = self.xmlHelper._getTextFromTagName('vendor_name')
         self.energyMeter.vendor_model = self.xmlHelper._getTextFromTagName('vendor_model')
      except XMLHelperException:
         pass
      return self.energyMeter


