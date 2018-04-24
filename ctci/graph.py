class Graph:
    def __init__(self, vertices = None, directed = True):
        self.vertices = {v:[] for v in vertices}
        if directed:
            self.directed = True
        else:
            self.directed = False

    def getVertices(self):
        return self.vertices

    def getEdges(self,v):
        return self.vertices[v]

    def setVertice(self,v):
        self.vertices[v] = {v:[]}

    def setEdge(self,v1,v2, weight = 0):
        self.vertices[v1].append([v2,weight])
        if not self.directed:
            self.vertices[v2].append([v1,weight])

    def __repr__(self):
        str = ''
        for v in self.vertices:
            str = str + "vertice %s: " % (v)
            edges = self.getEdges(v)
            for e in edges:
                str = str + " - %s,%s" % (e[0],e[1])
            str = str + '\n'
        return str

def main():
        graphy = Graph(['v1','v2','v3'])
        graphy.setEdge('v1','v2')
        graphy.setEdge('v1','v3')
        graphy.setEdge('v3','v2')

        print graphy
