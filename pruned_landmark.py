## Written By Xiangyu Zhang, Chao Fang
## For cs562 project


from priodict import priorityDictionary
from collections import defaultdict
import time
from dijkstra import graph, dijkstra
import random
import sys
from queue import Queue

def pruned_BFS(G, vk, L):
	Q = Queue()
	Q.put(vk)
	P = {}
	Lk = L.copy()
	for node in G.nodes:
		if node == vk:
			P[node] = 0.0
		else:
			P[node] = float("inf")
	while not Q.empty():
		u = Q.get()
		if u in L:
			#print("in1")
			if vk in L[u]:
				print("in2")
				if L[u][vk] <= P[u]:
					print("prun")
					continue
		Lk[u][vk] = P[u]
		for node in G.matrix[u]:
			if P[node] == float("inf"):
				P[node] = P[u] + G.matrix[u][node]
				Q.put(node)
	return Lk

def create_index(G):
	L = defaultdict(defaultdict)
	counter = 0
	for node in G.nodes:
		counter = counter+1
		print(counter)
		L = pruned_BFS(G, node, L)
	return L


def main():
	f = open("small.txt", "r")
	data = []
	for line in f:
		data.append(line)
	G = graph()
	for edge in data:
		edge = edge.split(" ")
		edge[3] = edge[3][:-1]
		G.add_edge(edge[1], edge[2], float(edge[3]))

	index = create_index(G)
	print(index)

if __name__ == "__main__":  
    main()






















