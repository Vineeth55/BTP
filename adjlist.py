#This programme converts all the benchmark circuits in edgelist format to AdjacencyList format.

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--X", default="/home/vineeth/Desktop/BTP/edgelist/", type=str, help="Read benchmark circuit in edgelist format in benchmark format from this directory")
parser.add_argument("--Y", default="/home/vineeth/Desktop/BTP/adjacencyList/", type=str, help="Write benchmark circuit in adjacency list format in this directory")

args = parser.parse_args()

X = args.X
Y = args.Y

dir_list = os.listdir(X)

for file in dir_list:
	fileaddr = X + file
	file1 = open(fileaddr, 'r')
	graph = nx.DiGraph()
	lines_list = file1.readlines()
	for line in lines_list:
		line1 = line.split()
		graph.add_edge(int(line1[0]), int(line1[1]))
	pos = file.find(".")
	name = file[8:pos]
	file1.close()
	waddr = Y + name + ".txt"
	nx.write_adjlist(graph, waddr)
	print(name + " Done")
 

