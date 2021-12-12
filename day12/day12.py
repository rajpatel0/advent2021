import networkx as nx
import matplotlib.pyplot as plt 
with open('input.txt', 'r') as f:
    data = f.readlines()

dataClean = [val.rstrip() for val in data]

G = nx.Graph()
for row in dataClean:
    start,end = row.split('-')
    G.add_node(start)
    G.add_node(end)
    G.add_edge(start,end)

def getPath(curNode,visited):
    if curNode == 'end':
        return 1
    if curNode.islower():
        visited = visited+[curNode]
    count = 0
    for neighbor in G.neighbors(curNode):
        if (neighbor not in visited):
            count += getPath(neighbor,visited)
    return count

def getPathPt2(curNode,visited):
    if curNode == 'end':
        return 1
    if curNode.islower():
        visited = visited+[curNode]
    count = 0
    for neighbor in G.neighbors(curNode):
        if (neighbor not in visited) or (neighbor != 'start' and len(visited)==len(set(visited))):
            count += getPathPt2(neighbor,visited)
    return count

smallVisited = []
print(getPath('start',smallVisited))
print(getPathPt2('start',smallVisited))





#just for reference simple paths is without reusing node
paths = nx.all_simple_paths(G,source='start',target='end')
print(len(list(paths)))