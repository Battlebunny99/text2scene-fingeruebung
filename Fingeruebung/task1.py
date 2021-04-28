import spacy
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_sm")

targetFile = "./Traning/RFC/Bicycles.xml"

tree = ET.parse(targetFile)
root = tree.getroot()
doc = nlp(root[0].text)

# POS
posDict = {}

print("POS:")
print("--------------------------")

for token in doc:
    if token.pos_ in posDict:
        posDict[token.pos_] = posDict[token.pos_] + 1
    else:
        posDict[token.pos_] = 1

for key in posDict:
    print(key, ":", posDict[key])
