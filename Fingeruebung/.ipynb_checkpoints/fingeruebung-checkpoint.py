import numpy
import matplotlib.pyplot as plt
import torch
import tensorflow as tf
import spacy
import networkx as nx
import xml.etree.ElementTree as ET
import itertools


def count_pos(ls):
     x_set = set(ls)
     x_dict = {}

     for entry in x_set:
          x_dict[entry] = ls.count(entry)

     return x_dict


# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Read document from xml file
tree = ET.parse('Training/RFC/Bicycles.xml')
root = tree.getroot()

# Extract text from file
text = root[0].text
doc = nlp(text)

# Analyze syntax


# part 1
ls = []
for token in doc:
     ls.append(token.pos_)
temp = count_pos(ls)
print("Aufgabe 1:", temp)
print("-----------------------------------------------------\n")


# part 2 - entities
ls = []

for elem in root[1]:
     ls.append(elem.tag)

temp = count_pos(ls)
print("Aufgabe 2:", temp)
print("-----------------------------------------------------\n")


# part 3 - qslinks
ls = []
for elem in root[1]:
     if elem.tag == "QSLINK":
          ls.append(elem.attrib['relType'])

temp = count_pos(ls)
print("Aufgabe 3:", temp)
print("-----------------------------------------------------\n")


# part 4 - satzlänge
ls = []
for sent in doc.sents:
     str = sent.text
     str2 = str.replace(' ', '')
     spaces = len(str) - len(str2)
     ls.append(spaces+1)

temp = count_pos(ls)
plt.bar(list(temp.keys()), list(temp.values()))
plt.title("Satzlängen")
plt.xlabel("Satzlängen")
plt.ylabel("Häufigkeiten")
print("Aufgabe 4:")
print("-----------------------------------------------------\n")
plt.show()


# part 5 - trigger
qs_trigger = []
o_trigger = []

# collect all triggers
for elem in root[1]:
     if elem.tag == "QSLINK":
          qs_trigger.append(elem.attrib['trigger'])
     elif elem.tag == "OLINK":
          o_trigger.append(elem.attrib['trigger'])
# turn it into dict and count how often they appear
qs_trigger = count_pos(qs_trigger)
o_trigger = count_pos(o_trigger)
# turn id into text in the dict
for elem in root[1]:
     if elem.tag == "SPATIAL_SIGNAL":
          for key in qs_trigger:
               if elem.attrib['id'] == key:
                    qs_trigger[elem.attrib['text']] = qs_trigger.pop(key)
                    break
          for key in o_trigger:
               if elem.attrib['id'] == key:
                    o_trigger[elem.attrib['text']] = o_trigger.pop(key)
                    break

print("Aufgabe 5:")
print("Qslink trigger:", qs_trigger)
print("Olink trigger:", o_trigger)
print("-----------------------------------------------------\n")

# part 6 - motion verb

verbs = []  # collect all different motion verbs
lemma_verbs = []   # only collect lemma from verbs
for elem in root[1]:
     if elem.tag == "MOTION":
          verbs.append(elem.attrib['text'])

for token in doc:
     if token.text in verbs:
          lemma_verbs.append(token.lemma_)

temp = count_pos(lemma_verbs)
temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
print("Aufgabe 6:", temp[0:5])
print("-----------------------------------------------------\n")



# Visualisierung
G = nx.Graph()
color_map = []
counter = 0
for elem in root[1]:
     if elem.tag == "SPATIAL_ENTITY":
          G.add_node(elem.attrib['text'])

nx.draw(G, node_color='r', with_labels=True)

for elem in root[1]:
     if elem.tag == "PLACE":
          G.add_node(elem.attrib['text'])

nx.draw(G, node_color='b', with_labels=True)


for elem in root[1]:
     if elem.tag == "LOCATION":
          G.add_node(elem.attrib['text'])

nx.draw(G, node_color='g', with_labels=True)


for elem in root[1]:
     if elem.tag == "PATH":
          G.add_node(elem.attrib['text'])

nx.draw(G, node_color='w', with_labels=True)


for elem in root[1]:
     if elem.tag == "NONMOTIONEVENT":
          G.add_node(elem.attrib['text'])

nx.draw(G, node_color='y', with_labels=True)


plt.show()