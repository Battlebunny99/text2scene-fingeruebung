import spacy
import xml.etree.ElementTree as ET
import numpy as np

nlp = spacy.load("en_core_web_sm")

targetFile = "./Traning/RFC/Bicycles.xml"

tree = ET.parse(targetFile)
root = tree.getroot()
doc = nlp(root[0].text)

# Motion
mtDict = {}

print("")
print("Top 5 MOTION:")
print("--------------------------")

for motion in root[1]:
    if motion.tag == "MOTION_SIGNAL":
        if motion.attrib["text"] in mtDict:
            mtDict[motion.attrib["text"]] = mtDict[motion.attrib["text"]] + 1
        else:
            mtDict[motion.attrib["text"]] = 1

mtDict = dict(
            sorted(
                mtDict.items(), 
                key=lambda item: item[1],
                reverse=True
            )[:5]
        )

for key in mtDict:
    print(key, ":", mtDict[key])
