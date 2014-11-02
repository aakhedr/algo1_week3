class Node(object):
    def __init__(self, name):
        self.name = name 
    def getName(self):
        return seflf.name    
    def __str__(self):
        return self.name    
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0} ->{1}'.format(self.src, self.dest)
    def __hash__(self):
        return self.name.__hash__()

class Graph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}    
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if src not in self.nodes:
            raise ValueError('source is not in graph')
        if dest not in self.nodes:
            raise ValueError('destination is not in graph')            
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def allEdges(self):
        edges = []
        for i in self.edges:
            for j in xrange(len(self.edges[i])):
                edges.append((i, self.edges[i][j]))
        return edges
    def __str__(self):
        res = ''
        for i in self.edges:
            for j in self.edges[i]:
                res = '{0}{1}->{2}\n'.format(res, i, j)
        return res[:-1]