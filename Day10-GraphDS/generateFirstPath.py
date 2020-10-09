# Program to generate the first path of the graph from the nodes provided
graph = {
    'a': ['c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['a', 'd'],
    'e': ['b', 'c']
}
# function to find path
def findPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        newPath = findPath(graph, node, end, path)
        if newPath:
            return newPath
        else: 
            return None

#function call to print the path
print(findPath(graph, 'd', 'c'))

            
        

