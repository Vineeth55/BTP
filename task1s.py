#This programme outputs the edgelist of a benchmark circuit
#when it is represented as a graph in networkx format

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--X", default="/home/vineeth/Desktop/BTP/bench/b14.bench", type=str, help="Read circuit in benchmark format from this file")

args = parser.parse_args()

X = args.X



file1 = open(X, 'r')
offset = 0

lines_list = file1.readlines()

inputs = int(lines_list[1].split()[1])
outputs = int(lines_list[2].split()[1])
dffs = int(lines_list[3].split()[1])
inverters = int(lines_list[4].split()[1])
gates = int(lines_list[5].split()[1])

graph = nx.DiGraph()
ncount = 0
Dict = {}

if inputs != 0:
	offset += 1


for i in range(6 + offset, 6 + offset + inputs):
	line = lines_list[i][6:-2].strip()
	nodeid = (line)
	if nodeid not in Dict.keys():
		ncount += 1
		graph.add_node(ncount, label=ncount, layer = 0)
		Dict[nodeid] = ncount

if outputs != 0:
	offset += 1

for i in range(6+inputs+offset, 6 + inputs + outputs + offset):
	line = lines_list[i][7:-2].strip()
	nodeid = (line)
	if nodeid not in Dict.keys():
		ncount += 1
		graph.add_node(ncount, label=ncount)
		Dict[nodeid] = ncount	


if inverters != 0 or gates != 0 or dffs != 0:
	offset += 1




for i in range(6+inputs+outputs+offset, 6+inputs+outputs+inverters+gates+dffs+offset):
	line = lines_list[i].split(" = ")

	res = (line[0]).strip()
	if res not in Dict.keys():
		ncount += 1
		graph.add_node(ncount, label=ncount)
		Dict[res] = ncount

	pos = line[1].find('(')
	gate = line[1][:pos]
	gateinputs = line[1][pos+1:-2].split(",")
	for j in range(len(gateinputs)):
		id = gateinputs[j].strip()
		if id not in Dict.keys():
			ncount += 1
			graph.add_node(ncount, label=ncount)
			Dict[id] = ncount
		graph.add_edge(Dict.get(gateinputs[j].strip()), Dict.get(res)) 

	# if gate == "NAND":
	# 	# ncount += 1
	# 	gateid = '~^' + str(ncount)
	# 	# graph.add_node(gateid, label=ncount)
	# 	# Dict[ncount] = gateid
	# 	# graph.add_edge(gateid, res)
	# 	for j in range(len(gateinputs)):
	# 		graph.add_edge(int(gateinputs[j]), res)

	# if gate == "NOT":
	# 	# ncount += 1
	# 	gateid = '~' + str(ncount)
	# 	# graph.add_node(gateid, label=ncount)
	# 	# Dict[ncount] = gateid
	# 	# graph.add_edge(gateid, res)
	# 	for j in range(len(gateinputs)):
	# 		graph.add_edge(int(gateinputs[j]), res)

	# if gate == "AND":
	# 	# ncount += 1
	# 	gateid = '^' + str(ncount)
	# 	# graph.add_node(gateid, label=ncount)
	# 	# Dict[ncount] = gateid
	# 	# graph.add_edge(gateid, res)
	# 	for j in range(len(gateinputs)):
	# 		graph.add_edge(int(gateinputs[j]), res)

	# if gate == "NOR":
	# 	# ncount += 1
	# 	gateid = '~v' + str(ncount)
	# 	# graph.add_node(gateid, label=ncount)
	# 	# Dict[ncount] = gateid
	# 	# graph.add_edge(gateid, res)
	# 	for j in range(len(gateinputs)):
	# 		graph.add_edge(int(gateinputs[j]), res)

	# if gate == "XOR":
	# 	# ncount += 1
	# 	gateid = '0+' + str(ncount)
	# 	# graph.add_node(gateid, label=ncount)
	# 	# Dict[ncount] = gateid
	# 	# graph.add_edge(gateid, res)
	# 	for j in range(len(gateinputs)):
	# 		graph.add_edge(int(gateinputs[j]), res)

	# if gate == "OR":
	# 	# ncount += 1
	# 	gateid = 'v' + str(ncount)
	# 	# graph.add_node(gateid, label=ncount)
	# 	# Dict[ncount] = gateid
	# 	# graph.add_edge(gateid, res)
	# 	for j in range(len(gateinputs)):
	# 		graph.add_edge(int(gateinputs[j]), res)

	# if gate == "BUFF":
	# 	# ncount += 1
	# 	gateid = '=' + str(ncount)
	# 	# graph.add_node(gateid, label=ncount)
	# 	# Dict[ncount] = gateid
	# 	# graph.add_edge(gateid, res)
	# 	for j in range(len(gateinputs)):
	# 		graph.add_edge(int(gateinputs[j]), res) 

	
	


nx.write_edgelist(graph, 'edgelistb14.edgelist')
# nx.draw_networkx(graph)
# plt.show()


file1.close()


