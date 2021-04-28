import spacy
import xml.etree.ElementTree as ET
from graphviz import Digraph

nlp = spacy.load("en_core_web_sm")

targetFile = "./Traning/ANC/WhereToMadrid/Highlights_of_the_Prado_Museum.xml"

tree = ET.parse(targetFile)
root = tree.getroot()
doc = nlp(root[0].text)

# Nodes
# https://networkx.org/documentation/networkx-2.3/tutorial.html#drawing-graphs

dot = Digraph('G', filename='PradoMuseum.gv', engine='sfdp')

dot.edge_attr.update(arrowhead="normal", arrowsize='1')

nodes_meta = {
    "PLACE": {
        "color": "red"
    },
    "LOCATION": {
        "color": "green"
    },
    "SPATIAL_ENTITY": {
        "color": "blue"
    },
    "NONMOTION_EVENT": {
        "color": "purple"
    },
    "PATH": {
        "color": "grey"
    },
}

nodes = []
edges = []

for elm in root[1]:
    if elm.tag in nodes_meta.keys():
        nodes.append((elm.attrib["id"], elm.attrib["text"], nodes_meta[elm.tag]["color"]))

for elm in root[1]:
    if elm.tag == "QSLINK" or elm.tag == "OLINK":
        edges.append(((elm.attrib["fromID"], elm.attrib["fromText"]), (elm.attrib["toID"], elm.attrib["toText"]), elm.attrib["relType"]))

changedSomething = True

while(changedSomething):
    changedSomething = False

    for elm in root[1]:
        if elm.tag == "METALINK":
            for node in nodes:
                if node[0] == elm.attrib["fromID"]:
                    nodes.remove(node)
                    changedSomething = True
                    nodes.append((elm.attrib["toID"], elm.attrib["toText"], node[2]))

            for edge in edges:
                if elm.attrib["fromID"] == edge[0][0]:
                    edges.remove(edge)
                    changedSomething = True
                    edges.append(((elm.attrib["toID"], elm.attrib["toText"]), (edge[1][0], edge[1][1]), edge[2])) 
                elif elm.attrib["fromID"] == edge[1][0]:
                    edges.remove(edge)
                    changedSomething = True
                    edges.append(((edge[0][0], edge[0][1]), (elm.attrib["toID"], elm.attrib["toText"]), edge[2]))

nodes = list(set(nodes))

for node in nodes:
    dot.node(node[0], node[1], fillcolor=node[2], color=node[2])


for edge in edges:
    #print(edge)
    dot.edge(edge[0][0], edge[1][0], label=edge[2])

dot_ = dot.unflatten(stagger=2)
dot_.view()