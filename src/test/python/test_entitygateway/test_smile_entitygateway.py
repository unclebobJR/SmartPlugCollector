import unittest
from xml.dom.minidom import parse, parseString
from entity.gasmeter import GasMeter
from entitygateway.xml_helper import XMLHelperException
from entity.electricitymeter import ElectricityMeter
from entity.energy_log import EnergyLog
from entitygateway.smile_energymetergateway import GasMeterGateway, ElectricityMeterGateway
from entitygateway.smile_entitygateway import SmileEntityGateway

class TestGasMeterGateway(unittest.TestCase):
      
  def test_givenTwoModules_expectException(self):
    gmg = GasMeterGateway(parseString("<modules><module id='1'></module><module id='2'></module></modules>"))
    self.assertRaises(XMLHelperException, gmg.getEnergyMeter)
     
  def test_givenModuleNoID_expectEmptyGasMeter(self):
    gmg = GasMeterGateway(parseString('<module></module>'))
    self.assertEqual(gmg.getEnergyMeter(), GasMeter())
     
  def test_givenXMLSmileData_expectGasMeter(self):
    gmg = GasMeterGateway(parse('test_entitygateway/smile_gasmodule.xml'))
    gm = GasMeter()
    gm.id = "c9340d0dfc0742FAKE97bda1ddb782"
    gm.logs.add(EnergyLog("2014-10-12T11:15:00+00:00", "2012-12-06T16:00:00+00:00", \
                          "2014-10-12T11:00:00+00:00", "2014-10-12T11:00:00+00:00", \
                          1967.35, "m3", "meterreading", "consumed"))
    self.assertEqual(gmg.getEnergyMeter(), gm)
      
class TestElectricityMeterGateway(unittest.TestCase):

  def test_givenTwoModules_expectException(self):
    emg = ElectricityMeterGateway(parseString("<modules><module id='1'></module><module id='2'></module></modules>"))
    self.assertRaises(XMLHelperException, emg.getEnergyMeter)
    
  def test_givenModuleNoID_expectEmptyElectricityMeter(self):
    emg = ElectricityMeterGateway(parseString('<module></module>'))
    self.assertEqual(emg.getEnergyMeter(), ElectricityMeter())
    
  def test_givenXMLSmileData_expectElectricityMeter(self):
    emg = ElectricityMeterGateway(parse('test_entitygateway/smile_electricitymodule.xml'))
    em = ElectricityMeter()
    em.id = "bd906d681e7a4FAKE29b319a917f5c0"
    em.vendor_model = r"ISk5\2ME382-1003"
    em.vendor_name = "ISkra"
    em.logs.add(EnergyLog("2014-10-12T11:15:00+00:00", "2012-12-06T16:00:00+00:00", \
                          "2014-10-12T11:22:28+00:00", "2014-10-12T11:22:28+00:00", \
                          4178042, "Wh", "meterreading", "consumed", "nl_offpeak"))
    em.logs.add(EnergyLog("2014-10-12T11:15:00+00:00", "2012-12-06T16:00:00+00:00", \
                          "2014-10-12T11:22:28+00:00", "2014-10-12T11:22:28+00:00", \
                          5226755, "Wh", "meterreading", "consumed", "nl_peak"))
    em.logs.add(EnergyLog("2014-10-12T11:15:00+00:00", "2012-12-06T16:00:00+00:00", \
                          "2014-10-12T11:22:28+00:00", "2014-10-12T11:22:28+00:00", \
                          1803, "Wh", "meterreading", "produced", "nl_offpeak"))
    em.logs.add(EnergyLog("2014-10-12T11:15:00+00:00", "2012-12-06T16:00:00+00:00", \
                          "2014-10-12T11:22:28+00:00", "2014-10-12T11:22:28+00:00", \
                          0, "Wh", "meterreading", "produced", "nl_peak"))  
    em.logs.add(EnergyLog("2014-10-12T11:15:00+00:00", "2012-12-06T16:00:00+00:00", \
                          "2014-10-12T11:22:28+00:00", "2014-10-12T11:22:28+00:00", \
                          450, "W", "currentvalue", "consumed"))
    em.logs.add(EnergyLog("2014-10-12T11:15:00+00:00", "2012-12-06T16:00:00+00:00", \
                          "2014-10-12T11:22:28+00:00", "2014-10-12T11:22:28+00:00", \
                          0, "W", "currentvalue", "produced"))
    self.assertEqual(emg.getEnergyMeter(), em)
      
class TestSmileEntityGateway(unittest.TestCase):
  def test_givensmileData_expectEnergyMeters(self):
    seg = SmileEntityGateway()
    seg.smileXMLData = self.getTextFromFile('smile.xml')
    modules = seg.getEnergyMeters()
    self.assertEqual(len(modules), 2)
    self.assertIsInstance(modules[0], GasMeter)
    self.assertIsInstance(modules[1], ElectricityMeter)

  def getTextFromFile(self, filePath):
    with open(filePath, 'r') as content_file:
      content = content_file.read()
    return content