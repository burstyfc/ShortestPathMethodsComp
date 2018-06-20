## Written By Xiangyu Zhang, Chao Fang
## For cs562 project
from dijkstra import graph, dijkstra
import ast

all_Label = {}
prev_label = {}
def init_hop_doubling_label(graph):
    global prev_label, all_Label

    for node in graph.nodes:
        # Initialize labels 
        all_Label[node] = {}
        prev_label[node] = {}

    # Initialization process
    for node in graph.nodes:
        neighbors = graph.matrix[node].keys()
        for nb in neighbors:
            dist = graph.matrix[node][nb]
            all_Label[node][nb] = dist
            prev_label[node][nb] = dist

# Get distance from Label
def get_distance(label, n1, n2):
    max_dist = 10000
    if (n2 in label[n1].keys()):
        max_dist = label[n1][n2]

    return max_dist

def node_ranking(graph, node):
    degree = len(graph.matrix[node])
    return degree

def update_hop_doubling(graph):
    global prev_label, all_Label
    count = 1
    while len(prev_label) != 0:
        print('label iteration ' + str(count))
        temp = {}
        for pn1 in prev_label:
            for pn2 in prev_label[pn1]:
                for an1 in all_Label:
                    for an2 in all_Label[an1]:
                        # Rule 1:
                        if (pn1 == an2 and node_ranking(graph, pn1) < node_ranking(graph, pn2) and
                                    node_ranking(graph, an1) >= node_ranking(graph, an2) and pn2 != an1 and
                                        prev_label[pn1][pn2] + all_Label[an1][an2] < get_distance(all_Label, an1, pn2)):
                            temp[an1] = {}
                            temp[an1][pn2] = prev_label[pn1][pn2] + all_Label[an1][an2]
                        # Rule 2:
                        elif (pn1 == an2 and node_ranking(graph, pn1) < node_ranking(graph, pn2) and
                                      node_ranking(graph, an1) < node_ranking(graph, an2) and pn2 != an1 and
                                          prev_label[pn1][pn2] + all_Label[an1][an2] < get_distance(all_Label, an1, pn2)):
                            temp[an1] = {}
                            temp[an1][pn2] = prev_label[pn1][pn2] + all_Label[an1][an2]
                        # Rule 4:
                        elif (pn2 == an1 and node_ranking(graph, pn1) >= node_ranking(graph, pn2) and
                                      node_ranking(graph, an1) < node_ranking(graph, an2) and pn1 != an2 and
                                          prev_label[pn1][pn2] + all_Label[an1][an2] < get_distance(all_Label, pn1, an2)):
                            temp[pn1] = {}
                            temp[pn1][an2] = prev_label[pn1][pn2] + all_Label[an1][an2]
                        # Rule 5:
                        elif (pn2 == an1 and node_ranking(graph, pn1) >= node_ranking(graph, pn2) and
                                      node_ranking(graph, an1) >= node_ranking(graph, an2) and pn1 != an2 and
                                          prev_label[pn1][pn2] + all_Label[an1][an2] < get_distance(all_Label, pn1, an2)):
                            temp[pn1] = {}
                            temp[pn1][an2] = prev_label[pn1][pn2] + all_Label[an1][an2]

            # print('an1: {0}, an2: {1}, pn1: {2}, pn2: {3} Done'.format(an1, an2, pn1, pn2))

            progress = float((list(prev_label.keys()).index(pn1) / len(prev_label)))
            progress *= 100
            
            #print('Labeling progress: ' +  str(progress) + '%')
            if len(temp) % 50 == 0:
                print(len(temp))

            # print(len(temp))
        # Update allLabel and Prevlabel
        count += 1
        print(str(len(temp)) + '--------------------------')
        prev_label = temp
        for tn1 in temp.keys():
            for tn2 in temp[tn1].keys():
                all_Label[tn1][tn2] = temp[tn1][tn2]            
      
        # Todo Label Pruning

    f = open("hop_doubling.txt", "w+")
    f.write(str(all_Label))
    f.close
    
def query(index, s, t, prev, stopper):
    # print('Current start node: ' + s)

    if (stopper == 100):
        return 10000

    dist = float('inf')
    if (s == t):
        return  0.0
    elif (t in index[s]):
        return index[s][t]
    else:
        for nb in index[s]:
            if nb in prev:
                continue
            else:
                prev.append(s)
                temp = index[s][nb] + query(index, nb, t, prev, stopper+1)
                if temp < dist:
                    dist = temp

        return dist


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

    sorted_l = sorted(G.matrix, key=lambda x: len(G.matrix[x]), reverse=True)
    # print(G.node_ranking('5'))
    # print(G.printGraph())
    # init_hop_doubling_label(G)
    # update_hop_doubling(G)

    with open('hop_doubling.txt', encoding='utf8') as f:
        index = f.readlines()[0]
    index = ast.literal_eval(index)


    result = query(index, '10000', '10010', [], 0)
    print(result)
    d, p = dijkstra(G, '0')
    print(d['14'])

main()
