from graph2 import Graph
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

def topologicalSort(graph, list):
    for v in graph:
        v.setColor('white')

    for v in graph:
        if v.getColor() == 'white':
            DFS(graph,list,v)

def DFS(graph, list, v):
    v.setColor('black')
    connections = v.getConnections()
    for c in connections:
        if c.getColor() == 'white':
            DFS(graph,list,c)
    list.append(v.getId())

def main():
    projects = Graph()
    projects.addVertex('a')
    projects.addVertex('b')
    projects.addVertex('c')
    projects.addVertex('d')
    projects.addVertex('e')
    projects.addVertex('f')

    projects.addEdge('f','a')
    projects.addEdge('a','d')
    projects.addEdge('f','b')
    projects.addEdge('b','d')
    projects.addEdge('d','c')

    projectList = []

    topologicalSort(projects, projectList)

    length = len(projectList)

    for i in xrange(length/2):
        projectList[i],projectList[length-i-1] = projectList[length-i-1],projectList[i]

    print projectList

main()
