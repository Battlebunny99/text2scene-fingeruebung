import spacy
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, text
import xml.etree.ElementTree as ET
import numpy as np
import networkx as nx

nlp = spacy.load("en_core_web_sm")

targetFile = "./Traning/RFC/Bicycles.xml"

tree = ET.parse(targetFile)
root = tree.getroot()
doc = nlp(root[0].text)

# Nodes
# https://networkx.org/documentation/networkx-2.3/tutorial.html#drawing-graphs

g = nx.Graph()

figure(figsize=(20, 12), dpi=80)

nodes = {
    "PLACE": {
        "color": "#D3C0D2",
        "nodes": []
    },
    "LOCATION": {
        "color": "#BB4430",
        "nodes": []
    },
    "SPATIAL_ENTITY": {
        "color": "#7EBDC2",
        "nodes": []
    },
    "NONMOTIONEVENT": {
        "color": "#F3DFA2",
        "nodes": []
    },
    "PATH": {
        "color": "#E2B6CF",
        "nodes": []
    },
}

nodesLabels = list(nodes.keys())

edges = []

for elm in root[1]:
    if elm.tag in nodes:
        nodes[elm.tag]["nodes"].append((elm.attrib["text"], {
            "id": elm.attrib["id"]
        }))
    elif elm.tag == "QSLINK" or elm.tag == "OLINK":
        #edges.append(elm.attrib["relType"])

        g.add_edge(elm.attrib["fromID"], elm.attrib["toID"], color="#919A9E", weight=1, label=elm.attrib["relType"])

for key in nodes:
    options = {
        'node_color': nodes[key]["color"],
        'node_size': 100,
        'width': 3,
    }

    g.add_nodes_from(nodes[key]["nodes"])

    pos = nx.spring_layout(g, k=50, iterations=100)

    for node, (x, y) in pos.items():
        text(x, y, node, fontsize=5, ha='center', va='center')

pos = nx.spring_layout(g, k=50, iterations=100)
nx.draw(g, **options, pos=pos, with_labels=False)

edgeLabels = nx.get_edge_attributes(g, "label")
nx.draw_networkx_edges(g, pos)
nx.draw_networkx_edge_labels(g, pos, edgeLabels, font_size=6)

plt.legend(nodesLabels, loc="upper left")

plt.show()