import unittest
from xml.dom.minidom import parseString
from entitygateway.factory_smile_entitygateway import EnergyMeterGatewayFactory, EnergyMeterGatewayFactoryException
from entitygateway.smile_energymetergateway import GasMeterGateway, ElectricityMeterGateway

class TestFactorySmileEntityGateway(unittest.TestCase):
  def setUp(self):
    self.segFac = EnergyMeterGatewayFactory()   
  
  def test_givenEmptyXMLModule_expectSEGException(self):
    self.assertRaises(EnergyMeterGatewayFactoryException, self.segFac.getEnergyMeterGateway, parseString("<module></module>"))
     
  def test_givenTwoXMLModules_expectSEGException(self):
    twoModDom = parseString("<modules>" + \
    "<module><cumulative_logs><cumulative_log><type>gas_consumed</type></cumulative_log></cumulative_logs></module>" + \
    "<module><cumulative_logs><cumulative_log><type>gas_consumed</type></cumulative_log></cumulative_logs></module>" + \
    "</modules>")
    self.assertRaises(EnergyMeterGatewayFactoryException, self.segFac.getEnergyMeterGateway, twoModDom)
  
  def test_givenXMLModuleOfWrongType_expectSEGException(self):
    modDom = parseString("<module><cumulative_logs><cumulative_log><type>consumed</type></cumulative_log></cumulative_logs></module>")
    self.assertRaises(EnergyMeterGatewayFactoryException, self.segFac.getEnergyMeterGateway, modDom)
  
  def test_givenXMLModuleForGas_expectSEGForGas(self):
    open('foo', 'a').close()
    xmlDom = self.getDomFromFile('test_entitygateway/smile_gasmodule.xml')
    seg = self.segFac.getEnergyMeterGateway(xmlDom)
    self.assertIsInstance(seg, GasMeterGateway)
  
  def test_givenXMLModuleForEL_expectSEGForElectricity(self):
    xmlDom = self.getDomFromFile('test_entitygateway/smile_electricitymodule.xml')
    seg = self.segFac.getEnergyMeterGateway(xmlDom)
    self.assertIsInstance(seg, ElectricityMeterGateway)  
  
  def getDomFromFile(self, filePath):
    with open(filePath, 'r') as content_file:
      content = content_file.read()
    dom = parseString(content)
    return dom
