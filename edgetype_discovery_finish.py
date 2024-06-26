class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.discovery_time = {}
        self.finish_time = {}
        self.time = 0
        self.parent = {}

    def add_edge(self, v, w):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[v].append(w)

    def DFS_visit(self, u, visited, edge_types):
        visited.add(u)
        self.time += 1
        self.discovery_time[u] = self.time
        for v in self.adjacency_list.get(u, []):
            if v not in visited:
                self.parent[v] = u
                edge_types[(u, v)] = 'Tree'
                self.DFS_visit(v, visited, edge_types)
            elif v in visited and v not in self.finish_time:
                edge_types[(u, v)] = 'Back'
            elif v in visited and self.discovery_time[u] < self.discovery_time[v]:
                edge_types[(u, v)] = 'Forward'
            elif v in visited and self.discovery_time[u] > self.discovery_time[v]:
                edge_types[(u, v)] = 'Cross'
        self.time += 1
        self.finish_time[u] = self.time

    def DFS(self):
        visited = set()
        edge_types = {}
        for u in self.adjacency_list:
            self.parent[u] = None
        for u in self.adjacency_list:
            if u not in visited:
                self.DFS_visit(u, visited, edge_types)
        return edge_types

# Create a graph
""" g1 = Graph()
g1.add_edge('a', 'b')
g1.add_edge('a', 'd')
g1.add_edge('b', 'c')
g1.add_edge('b', 'd')
g1.add_edge('d', 'e')
g1.add_edge('c', 'e')
g1.add_edge('e', 'f')
g1.add_edge('e', 'g')
g1.add_edge('e', 'b')
g1.add_edge('f', 'c')
g1.add_edge('f', 'h')
g1.add_edge('h', 'i')
g1.add_edge('h', 'e')
g1.add_edge('g', 'h')
g1.add_edge('g', 'd') """

letters = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
}
g = Graph()
g.add_edge('c','d')
g.add_edge('d','h')
g.add_edge('h','c')
g.add_edge('c','g')
g.add_edge('c','b')
g.add_edge('g','f')
g.add_edge('g','b')
g.add_edge('b','f')
g.add_edge('b','g')
g.add_edge('f','a')
g.add_edge('f','g')

# Run DFS and get edge types
edge_types = g.DFS()

# Print edge types
for edge, edge_type in edge_types.items():
    print(f"Edge {edge} is a {edge_type} edge.")

# Print discovery and finish times
for node in g.discovery_time:
    print(f"Node {node} has discovery time {g.discovery_time[node]} and finish time {g.finish_time[node]}.")

