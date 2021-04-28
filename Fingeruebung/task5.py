import spacy
import xml.etree.ElementTree as ET
import numpy as np

nlp = spacy.load("en_core_web_sm")

targetFile = "./Traning/RFC/Bicycles.xml"

tree = ET.parse(targetFile)
root = tree.getroot()
doc = nlp(root[0].text)

# Präposition
psDict = {}
siDict = {}

print("")
print("QSLinks/OLinks:")
print("--------------------------")

for elm in root[1]:
    if elm.tag == "SPATIAL_SIGNAL":
        if elm.attrib["id"] not in siDict:
            siDict[elm.attrib["id"]] = elm.attrib["text"]

for elm in root[1]:
    if elm.tag == "QSLINK" or elm.tag == "OLINK":
        if elm.tag in psDict:
            if elm.attrib["trigger"] in psDict[elm.tag]:
                psDict[elm.tag][elm.attrib["trigger"]]["count"] = psDict[elm.tag][elm.attrib["trigger"]]["count"] + 1
            elif len(elm.attrib["trigger"]) > 0:
                psDict[elm.tag][elm.attrib["trigger"]] = {}
                psDict[elm.tag][elm.attrib["trigger"]]["count"] = 1
        else:
            psDict[elm.tag] = {}
            psDict[elm.tag][elm.attrib["trigger"]] = {}
            psDict[elm.tag][elm.attrib["trigger"]]["count"] = 1
        
        if len(elm.attrib["trigger"]) > 0:
            psDict[elm.tag][elm.attrib["trigger"]]["text"] = siDict[elm.attrib["trigger"]]

for key in psDict:
    print("--", key, ":")
    for trigger in psDict[key]:
        print(trigger, ":", psDict[key][trigger])
