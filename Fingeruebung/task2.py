import spacy
import xml.etree.ElementTree as ET
import numpy as np

nlp = spacy.load("en_core_web_sm")

targetFile = "./Traning/RFC/Bicycles.xml"

tree = ET.parse(targetFile)
root = tree.getroot()
doc = nlp(root[0].text)

# TAGS
tagDict = {}

print("")
print("TAGS:")
print("--------------------------")

for tag in root[1]:
    if tag.tag in tagDict:
        tagDict[tag.tag] = tagDict[tag.tag] + 1
    else:
        tagDict[tag.tag] = 1

for key in tagDict:
    print(key, ":", tagDict[key])