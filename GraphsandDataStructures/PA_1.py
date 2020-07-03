"""
Graphs and Data Structures Course
Programming Assignment #1 - Numair Ahmed

The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11^{th}11 
th
  row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
-----------------------------------------------

Reverse engineering code from http://proserge.kh.ua/coding/index.php/post/41/Stanford+%22Algorithms%3A+Design+and+Analysis%22+week4 

"""

import collections #this provides specialized high-performance container datatypes alternative to the standard list, dict, tuple.
import sys
import random

def return_emptylist():
    return []

def return_false():
    return False

def ParseGraph(filename):
    #filename will be algo4SCC.txt, taken from the coursera website
    """Parse a graph into a list of edges for programming.
    Arguments taken: 
    - filename: the original graph given in the .txt file 
    Returns:
    - edges = [(vertex1, vertex2), (vertex2, vertext3), ....] represented as tuples.
    """

    edges = [] #instantiate an empty edges array
    for l in open(filename):
        fields = [int(f) for f in l.split()] #split each line of the file read and convert to int
        edges.append(tuple(fields)) #build a list of tuples consisting of the entries in the original graph

    #defaultdict is interesting bc you can initialize the dict with a list of tuples as the default_factory attribute. But im not sure how this is advantageous
    adjacency = collections.defaultdict(return_emptylist)
    reverse_adjacency = collections.defaultdict(return_emptylist)

    #im not quite sure what is happening here. i know it should be extracting edges in some way but this looks confusing.
    for e in edges:
        adjacency[e[0]] = adjacency[e[0]] + [e]
        reverse_adjacency[e[1]] = reverse_adjacency[e[1]] + [e[1], e[0]]

    return adjacency, reverse_adjacency, edges

t = 0 #is this the sink node?
s = 0 #is this the source node?
finishing = {} #created as a set but im not sure why set was chosen as the data structure of choice.
leader = {} #created as a set
explored = collections.defaultdict(return_false)

def ResetState():
    global t,s,finishing, leader, explored
    t = 0
    s = 0
    finishing = {}
    leader = {}
    explored = collections.defaultdict(return_false)

def DFSLoop(edges, labeling, reversed = False):
    global s 
    for i in labeling: #what is labeling?
        print("Looking at node: " + str(i) + "\n") #+ " labeling is: " + str(type(labeling))
        if not explored[i]: #if there is such an element i from 'labeling' that is not present in the already explored list of nodes, then store that in s.
            s = i
            DFS(edges, i, reversed)

forward_adjacency = {}
reverse_adjacency = {}

def DFS(edges, start, reversed = False): #False is the default condition for Arg reversed. Start is the starting node. But how to determine that?
    global t
    if reversed:
        adjacency = reverse_adjacency
    else:
        adjacency = forward_adjacency
    #print("the adjacency list: " + str(type(adjacency)) + " len: " + str(len(adjacency)) + "\n")
    #print(adjacency)
    
    #iterative (i.e. manually managing a stack) solution
    stack = []
    stack.append((start, 1)) 
    #print("length of stack: " + str(len(stack)))
    #edge_counter = 0

    while len(stack) > 0:
        current, phase = stack.pop() #what the heck is phase and current?
        #print("entered while loop on len of stack>0 : \n")
        #print("current: " + str(current) + " phase: " +str(phase) + "\n")
        #print(edge_counter)
        if phase == 1: #what does phase being 1 signify?
            explored[current] = True 
            leader[current] = s
            #print("explored[current] " + str(explored[current]) + " leader[current] " + str(leader[current]) + "\n")
            edge_found = False #this is the default assumption to accomodate for solo nodes or ones that are connected to already visited nodes
            #print("entered if phase == 1 condition statement: \n")
            #print("adjacency[current]: ")
            #print(adjacency[current])
            #print("\nthe explored list of nodes so far: \n")
            #print(explored)
            for edge in adjacency[current]: #for every edge in the adjacency list corresponding to this current node
                #print("\nthe current edge: \n")
                #print(edge)
                #print("\nthe type of this edge: " + str(type(edge)))
                if not explored[edge]: #if its connected node doesn't exist in explored, then...
                    stack.append((current, 1)) #append this starting node to the stack
                    stack.append((edge, 1)) #then append this newly discovered node to the stack
                    edge_found = True #given we're at the current node, we have found a new node, therefore an edge is found. 
                    #edge_counter += 1
                    break 
            if not edge_found: #if no new node is found, therefore no new edge is traversed
                stack.append((current, 2)) #change phase state to 2 which indicates all of the new nodes connected to node current have been found
        #print("the associated stack: \n")
        #print(stack)
        if phase == 2:
            t += 1
            finishing[current] = t
            print('Finished ' + str(current) + "\n")

forward_adjacency, reverse_adjacency, edges = ParseGraph("week1.txt")

sys.stderr.write('Graph parsed.\n')

num_nodes = max([e[0] for e in edges] + [e[1] for e in edges])
labeling = range(num_nodes, 0, -1)
DFSLoop(edges, labeling, True) #note reversed argument is True in this case

sys.stderr.write('Reverse DFSLoop done\n')

inverse_finishing = dict((v,k) for k,v in finishing.items())
finish_labeling = [inverse_finishing[i] for i in range(num_nodes, 0, -1)]

ResetState()
DFSLoop(edges, finish_labeling) #note reversed argument is not input here, therefore it is False by default

sys.stderr.write('Forward DFSLoop also done.\n')

sccs = {}
for i in leader:
    if leader[i] not in sccs:
        sccs[leader[i]] = [i]
    else:
        sccs[leader[i]].append(i)

for i in sccs:
    print('%s\t%s' % (i, len(sccs[i])))

