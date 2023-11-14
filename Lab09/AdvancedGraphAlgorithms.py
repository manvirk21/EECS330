import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w


    def dijkstra(self, src):
        # Stores shortest distance.
        dist = [sys.maxsize] * self.V
        # Shortest distance to the same node is 0.
        dist[src] = 0
        
        # Priority queue to store vertices and their distances.
        priority_queue = [(0, src)]

        while priority_queue:
            # Extract the vertex with the smallest distance.
            distance, current_vertex = min(priority_queue)
            priority_queue.remove((distance, current_vertex))

            # Update the distance of adjacent vertices.
            for v in range(self.V):
                if self.graph[current_vertex][v] > 0:
                    if dist[current_vertex] + self.graph[current_vertex][v] < dist[v]:
                        dist[v] = dist[current_vertex] + self.graph[current_vertex][v]
                        priority_queue.append((dist[v], v))

        # You have to call print_solution by passing dist.
        # In this way everyone's output would be standardized.
        self.print_dijkstra(dist)

    def print_dijkstra(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t->\t {dist[node]}")



    def prim(self):
        # Store the resulting graph.
        # where result[i] keeps the source vertex.
        # See the example output for expected result.
        result = [None] * self.V
        # Key values used to pick minimum weight edge in cut.
        key = [sys.maxsize] * self.V
        # To represent set of vertices included in MST.
        mst_set = [False] * self.V

        # Choose the first vertex as the starting point.
        key[0] = 0
        result[0] = -1  # No parent for the first vertex.

        for cout in range(self.V):
            # Pick the minimum key vertex from the set of vertices not yet included in MST.
            u = self.min_key(key, mst_set)

            # Add the picked vertex to the MST set.
            mst_set[u] = True

            # Update key value and result index of the adjacent vertices of the picked vertex.
            for v in range(self.V):
                if self.graph[u][v] > 0 and mst_set[v] is False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    result[v] = u

        # You have to call print_solution by passing the output graph.
        # In this way everyone's output would be standardized.
        self.print_prim(result)

    def min_key(self, key, mst_set):
        min_val = sys.maxsize

        for v in range(self.V):
            if key[v] < min_val and mst_set[v] is False:
                min_val = key[v]
                min_index = v

        return min_index

    def print_prim(self, result):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(f"{result[i]} - {i} \t {self.graph[i][result[i]]}")            



    def kruskal(self):
        result = []  # To store the resulting graph.

        # Helper function to find the set of an element i.
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        # Helper function to union two sets.
        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        # Sort all the edges in non-decreasing order of their weight.
        edges = []
        for i in range(self.V):
            for j in range(i+1, self.V):
                if self.graph[i][j] != 0:
                    edges.append((i, j, self.graph[i][j]))

        edges = sorted(edges, key=lambda x: x[2])

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while len(result) < self.V - 1:
            u, v, w = edges.pop(0)
            set_u = find(parent, u)
            set_v = find(parent, v)

            if set_u != set_v:
                result.append((u, v, w))
                union(parent, rank, set_u, set_v)

        self.print_kruskal(result)

    def print_kruskal(self, result):
        print("Edge \t Weight")
        for edge in result:
            print(f"{edge[0]} - {edge[1]} \t {edge[2]}")




# Create a graph with 21 vertices.
graph = Graph(21)

# Add edges and their weights.
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 5, 2)
graph.add_edge(4, 6, 2)
graph.add_edge(5, 7, 2)
graph.add_edge(7, 8, 2)
graph.add_edge(6, 8, 2)

graph.add_edge(8, 9, 5)
graph.add_edge(8, 10, 4)
graph.add_edge(9, 11, 3)
graph.add_edge(10, 11, 1)

graph.add_edge(11, 12, 1)
graph.add_edge(12, 13, 1)
graph.add_edge(13, 14, 1)

graph.add_edge(14, 15, 1)
graph.add_edge(14, 16, 10)
graph.add_edge(15, 17, 1)
graph.add_edge(16, 20, 1)
graph.add_edge(17, 18, 1)
graph.add_edge(18, 19, 1)
graph.add_edge(19, 20, 1)

# Run Dijkstra's algorithm from source vertex 0.
graph.dijkstra(0)

# Find and print the Prim's Minimum Spanning Tree (MST).
graph.prim()

# Find and print the Kruskal's Minimum Spanning Tree (MST).
graph.kruskal()
