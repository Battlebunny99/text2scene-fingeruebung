import spacy
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_sm")

targetFile = "./Traning/RFC/Bicycles.xml"

tree = ET.parse(targetFile)
root = tree.getroot()
doc = nlp(root[0].text)

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