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

# Sentences
ssDict = {}

print("")
print("Sentences:")
print("--------------------------")

for s in doc.sents:
    print("####", s, "####")
    print(len(s), len(list(s)))

    if len(s) in ssDict:
        ssDict[len(s)] = ssDict[len(s)] + 1
    else:
        ssDict[len(s)] = 1

x = []
y = []

for key in ssDict:
    x.append(key)
    y.append(ssDict[key])

y = tuple(y)

y_pos = np.arange(len(x))

plt.bar(y_pos, y)
plt.xticks(y_pos)

plt.show()

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


