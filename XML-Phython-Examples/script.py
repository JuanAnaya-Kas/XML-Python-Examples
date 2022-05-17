import xml.etree.ElementTree as ET
filename = "bookstore.xml"
xmlTree = ET.parse(filename)
rootElement = xmlTree.getroot() 
#Iterate Through All Books
for element in rootElement.findall("book"):
    #Check if title contains the word Python
        element.set('category','Python')
#Write the modified file.     
xmlTree.write(filename,encoding='UTF-8',xml_declaration=True) 