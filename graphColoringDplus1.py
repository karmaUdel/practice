def getDegree(graph):
    #nodes = graph
    degree = 0
    for node in graph:
        if degree < len(node.neighbors):
            degree = len(node.neighbors)
    return degree
    
def colorGraph(node,color,visited):
    if color:
        if node.color == None:
            visited[node.label] = color.pop(0)
            node.color = visited[node.label] # assign color
        neighbors = node.neighbors # get neighbours
        for neighbor in neighbors:
            print neighbor.label
            if not(neighbor.label in visited): # if neighbour is unique
                print neighbor.label
                print color
                if color: # color is not empty
                    neighbor.color = color.pop(0)
                    visited[neighbor.label] = neighbor.color
                else: #backtrack
                    return visited
    return visited
    

def my_function(arg):

    # Write the body of your function here
    degree = getDegree(arg)
    visited = {} # node.label : color
    color = [i for i in range(0, degree+1,1)] # all colors
    print color
    #arg = colorGraph(arg,color,visited)
    for node in graph:
        print node
        visited = colorGraph(node,color,visited)
    #copy Colors
    for node in graph:
        if node.label in visited:
            node.color = visited[node.label]
    return arg

    #return 'running with %s' % arg
def print_my_function(graph):
    graph = my_function(graph)
    for node in graph:
        print(node.label, node.color)
# Run your function through some test cases here
# Remember: debugging is half the battle!
class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]
print_my_function(graph)
