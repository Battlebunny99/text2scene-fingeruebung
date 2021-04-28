import spacy
import xml.etree.ElementTree as ET
import numpy as np

nlp = spacy.load("en_core_web_sm")

targetFile = "./Traning/RFC/Bicycles.xml"

tree = ET.parse(targetFile)
root = tree.getroot()
doc = nlp(root[0].text)

# QsLink
qsDict = {}

print("")
print("QSLinks:")
print("--------------------------")

for tag in root[1]:
    if tag.tag == "QSLINK":
        if tag.attrib["relType"] in qsDict:
            qsDict[tag.attrib["relType"]] = qsDict[tag.attrib["relType"]] + 1
        else:
            qsDict[tag.attrib["relType"]] = 1

for key in qsDict:
    print(key, ":", qsDict[key])