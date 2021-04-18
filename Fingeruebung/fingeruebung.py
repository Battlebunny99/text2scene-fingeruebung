import numpy
import matplotlib.pyplot as plt
import torch
import tensorflow as tf
import spacy
import networkx as net
import xml.etree.ElementTree as ET

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
#for entity in doc.ents:
#    print(entity.text, entity.label_)


tree = ET.parse('Traning/RFC/Bicycles.xml')
root = tree.getroot()

# create a new XML file with the results
print(root.tag)
print(root.attrib)

#for child in root:
#        print(child.tag, child.attrib)

# print(root[0].text)

text = root[0].text
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)