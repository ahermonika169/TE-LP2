from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addVertex(self, v):
        self.graph[v]

    def DFS(self, v, d, visitSet = None) -> bool:
        visited = visitSet or set()
        visited.add(v)
        print(v,end=" ")

        if v == d:
            return True

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.DFS(neighbour, d, visited):
                    return True

        return False
    
    def BFS(self, s, d):
        visited = defaultdict(bool)
        queue = deque([s])
        visited[s] = True

        while queue:
            s = queue.popleft()
            print(s, end=' ')
            if s == d:
                return True
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return False
    
if __name__ == '__main__':
    g = Graph()

    n = int(input("Enter number of nodes: "))

    for i in range(n):
        node = input("Enter node {}: ".format(i+1))
        g.addVertex(node)

    e = int(input("\nEnter number of edges: "))

    for i in range(e):
        nodes = input("Enter edge {} (format: node1 node2): ".format(i+1)).split()
        g.addEdge(nodes[0], nodes[1])

    print("\nGraph input completed")

    s = input("Enter source node: ")
    d = input("Enter destination node: ")
    
    print("\nFollowing is Depth First Traversal {} -> {}:".format(s, d))
    g.DFS(s, d)
    

    print("\n\nFollowing is Breadth First Traversal {} -> {}:".format(s, d))
    g.BFS(s, d)
