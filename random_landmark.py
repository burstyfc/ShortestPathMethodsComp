## Written By Xiangyu Zhang, Chao Fang
## For cs562 project


from priodict import priorityDictionary
from collections import defaultdict
import time
from dijkstra import graph, dijkstra
import random
import sys

def random_select(G, num):
	nodes = list(G.nodes)
	picked = set()
	while len(picked) < num:
		idx = random.randint(0, (G.V - 1))
		picked.add(nodes[idx])
	return picked

def create_index(G, node_set):
	index = {}
	counter = 0
	for node in node_set:
		dist, prev = dijkstra(G, node)
		index[node] = (dist, prev)
		counter = counter+1
		print(counter)

	f= open("index.txt","w+")
	f.write(str(index))
	f.close
	return index



def query(index, u, v):
	mindist = float("inf")
	for i in index:
		temp = index[i][0][u] + index[i][0][v]
		if temp < mindist:
			mindist = temp
	return mindist


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

	idx_start_time = time.time()
	selected = random_select(G, 1000)
	index = create_index(G, selected)
	idx_end_time = time.time()
	idx_time = idx_end_time - idx_start_time

	q_start_time = time.time()
	result = query(index, "0", "21047")
	q_end_time = time.time()
	query_time = (q_end_time - q_start_time)*1000

	print("***From landmark_label***")
	print("query time: "+ str(query_time) +"ms")
	print("index time: "+ str(idx_time) +"s")
	print("The distance from node0 to node21047 is: " + str(result))


if __name__ == "__main__":  
    main()

