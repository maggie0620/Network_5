import re
file1 = open('D:/Network/Network 1.txt', 'r')
net1 = file1.read()

## 5-1
# Use network 1
# Derive two BFS trees
split1 = re.split('\n', net1)
split1.remove('')
edge1 = []
for i in range(0,len(split1)):
    num1 = re.sub('\t','',split1[i])
    edge1.append(num1)
    
mylist1 = []
for k in edge1:
    if k[0] not in mylist1:
        mylist1.append(k[0])
    if k[1] not in mylist1:
        mylist1.append(k[1])

# BFS
from collections import defaultdict

class Graph:
    def __init__(self, nodes, edges):
        self.graph = defaultdict(list)
        self.nodes = nodes
        for k in range(0,len(edges)):
            self.graph[edges[k][0]].append(edges[k][1])
    
    def BFS(self, start):
        visited = [False] * len(self.nodes)
        alist = []
        key = self.nodes.index(start)
        visited[key] = True
        alist.append(start)
        
        edge_visit = []
        while alist:
            v = alist.pop()
            for i in self.graph[v]:
                k = self.nodes.index(i)
                if not visited[k]:
                    visited[k] = True
                    alist.append(i)
                    edge_visit.append(v+i)
        return edge_visit
    
BFS_tree = Graph(mylist1, edge1) 
# Pick i and g node
tree1 = BFS_tree.BFS(mylist1[0])
print("BFS tree edge list from", mylist1[0], ":", tree1)
tree2 = BFS_tree.BFS(mylist1[2])
print("BFS tree edge list from", mylist1[2], ":", tree2)

# Use the started node as the 1st terminal, s
# Use the last added node as the 2nd terminal, t
start1 = tree1[0][0]
end1 = tree1[len(tree1)-1][1]
label = {}
for x in mylist1:
    if x == start1:
        label[x] = "s"
    elif x == end1:
        label[x] = "t"
    else:
        label[x] = x
#print(label)

# Tree1
new_tree1 = []
for string in tree1:
    name = label.get(string[0]),label.get(string[1])
    changed = "".join(name)
    new_tree1.append(changed)
print("Tree 1 (replaced by 's' and 't'):", new_tree1)

node_tree1 = []
for node in mylist1:
    name = label.get(node[0])
    changed = "".join(name)
    node_tree1.append(changed)
#print(node_tree1)

# Change the node name of tree2
start2 = tree2[0][0]
end2 = tree2[len(tree2)-1][1]
label = {}
count = 0
for x in mylist1:
    if x == start2:
        label[x] = "s"
    elif x == end2:
        label[x] = "t"
    else:
        label[x] = str(count)
    count += 1
#print(label)

# Tree2
new_tree2 = []
for string in tree2:
    name = label.get(string[0]),label.get(string[1])
    changed = "".join(name)
    new_tree2.append(changed)
print("Tree 2 (replaced by 's' and 't'):", new_tree2)

node_tree2 = []
for node in mylist1:
    name = label.get(node[0])
    changed = "".join(name)
    node_tree2.append(changed)
#print(node_tree2)


## Run series and parallel operation
# Series operation (Connect tree1 "t" and tree2 "s")
series_label1 = {}
for x in node_tree1:
    # Change tree1 "t" to "u"
    if x == "t":
        series_label1[x] = "u"
    else:
        series_label1[x] = x
#print(series_label1)

series_label2 = {}
for x in node_tree2:
    # Change tree2 "s" to "u"
    if x == "s":
        series_label2[x] = "u"
    else:
        series_label2[x] = x
#print(series_label2)

# Change tree1 label
series_tree1 = []
for string in new_tree1:
    name = series_label1.get(string[0]),series_label1.get(string[1])
    changed = "".join(name)
    series_tree1.append(changed)
#print("Series tree 1:", series_tree1)

# Change tree2 label
series_tree2 = []
for string in new_tree2:
    name = series_label2.get(string[0]),series_label2.get(string[1])
    changed = "".join(name)
    series_tree2.append(changed)
#print("Series tree 2:", series_tree2)

ser_tree = series_tree1.copy()
for edge in series_tree2:
    ser_tree.append(edge)
print("Series operation:", ser_tree)

# Parallel operation
para_tree = new_tree1.copy()
for edge in new_tree2:
    para_tree.append(edge)
print("Parallel operation:", para_tree)


## 5-2
# Write a program to produce a k-Tree graph (Input: k, n < k + 5 ; Output: a k-Tree graph)
import matplotlib.pyplot as plt
import numpy as np
import random

# Plot a clique with input k
k = int(input("Input k to get a k-tree graph: "))

# Produce a regular polygon
angle = np.linspace(0, 2 * np.pi, k, endpoint = False)
x = np.cos(angle)
y = np.sin(angle)

# Connect back to the origin
x = np.append(x, x[0])
y = np.append(y, y[0])
#print(x,y)

# Plot clique
fig = plt.subplot()
fig.plot(x, y, marker='o', color='k')
for i in range(0,len(x)-1):
    fig.text(x[i], y[i], 0, fontsize=14, ha='center', va='bottom')

# Get nodes position of clique 
nodes = []
for i in range(0,len(x)):
    pos = (x[i],y[i])
    nodes.append(pos)
nodes = nodes[:-1]    # Remove same position
#print(nodes)

# Create 5 new nodes
angle = np.linspace(0, 2 * np.pi, 6)
new_angle = angle + (np.pi/4)
x_add_node = 1.5 * np.cos(new_angle)
y_add_node = 1.5 * abs(np.sin(new_angle))

# Plot k-tree graph
num = 0
add_color = ["green","gold","blue","red","purple"] 
for i in range(0,len(x_add_node)-1):
    num += 1
    fig.plot(x_add_node[i], y_add_node[i], marker='o', color = add_color[i])
    fig.text(x_add_node[i], y_add_node[i], num, fontsize=14, ha='center', va='bottom')
    
    # Random select k nodes to connect
    selected_nodes = random.sample(nodes, k)
    for x_selected, y_selected in selected_nodes:
        fig.plot([x_selected, x_add_node[i]], [y_selected, y_add_node[i]], color = add_color[i])
    add_pos = (x_add_node[i],y_add_node[i])
    nodes.append(add_pos)

plt.axis('off')
plt.show()