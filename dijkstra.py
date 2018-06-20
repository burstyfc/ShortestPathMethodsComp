## Written By Xiangyu Zhang, Chao Fang
## For cs562 project
## used a little part from https://www.ics.uci.edu/~eppstein/161/python/dijkstra.py

from priodict import priorityDictionary
from collections import defaultdict
import time

class graph:
    def __init__(self):
        self.V = 0
        self.nodes = set()
        self.matrix = defaultdict(defaultdict)
        self.dist = defaultdict(defaultdict)


    def add_edge(self, from_node, to_node, distance):
        self.nodes.add(from_node)
        self.nodes.add(to_node)
        self.V = len(self.nodes)
        self.matrix[from_node][to_node] = distance
        self.matrix[to_node][from_node] = distance
        self.dist[(from_node, to_node)] = distance





def dijkstra(G, source):
    Q = priorityDictionary()
    prev = {}
    distances = {}
    Q[source] = 0.0
    for v in Q:
        distances[v] = Q[v]
        if v == None:
            break
        for w in G.matrix[v]:
            temp = distances[v] + G.matrix[v][w]
            if w in distances:
                if temp < distances[w]:
                    raise ValueError("Error")
            elif w not in Q or temp < Q[w]:
                Q[w] = temp
                prev[w] = v

    return (distances, prev)


def main():
    f = open("cal.cedge", "r")
    data = []
    for line in f:
        data.append(line)
    G = graph()
    for edge in data:
        edge = edge.split(" ")
        edge[3] = edge[3][:-1]
        G.add_edge(edge[1], edge[2], float(edge[3]))


    start_time = time.time()
    d, p = dijkstra(G, "0")
    end_time = time.time()
    running_time = (end_time - start_time)*1000


    print("***From dijkstra***")
    print("query time: "+ str(running_time) +"ms")
    print("The distance from node0 to node21047 is: " + str(d["8"]))

if __name__ == "__main__":
    main()

