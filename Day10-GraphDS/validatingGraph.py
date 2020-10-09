from collections import defaultdict
graph = defaultdict(list) #The type of this new entry is given by the argument of defaultdict. 
# function for adding edge to graph
def addEdge(graph,u,v):
    graph[u].append(v) #Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary. defaultdict allows that if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created.

# definition of function generate_edges
def generate_edges(graph):
    edges = []
    for node in graph:
        for nbr in graph[node]:
            edges.append((node, nbr))
    return edges

# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

print(*graph)
# Function call to print generated graph
print(generate_edges(graph))