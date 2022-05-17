#Import and config module ElementTree with alias ET
import xml.etree.ElementTree as ET
filename = 'Sync.AdvanceShipNotice.xml'
xmlTree = ET.parse(filename)
rootElement = xmlTree.getroot()
#INPORTANT register namespace atribute xmlns
ET.register_namespace('', 'http://schema.infor.com/InforOAGIS/2')
#Navegate to child node ReferenceID
ValuesChangesArr = []
ReferenceID = rootElement[0][0][2]
LocationID = rootElement[1][0][2]
Id = rootElement[1][1][0][0][0]
#Arr node titles 
TitlesArr = ['ReferenceID','LocationID','Id']
#Create arr with get nodes
ValuesChangesArr.extend([ReferenceID,LocationID,Id])
for titles in TitlesArr:
    ValuesChangesArr[TitlesArr.index(titles)].set('accountingEntity','AE2')
xmlTree.write(filename,encoding='UTF-8',xml_declaration=True) 
