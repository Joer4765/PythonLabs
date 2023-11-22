class Graph:
    def __init__(self, _adjacency_list: dict):
        self.adjacency_list = _adjacency_list
        self.vertices = sorted(set(list(self.adjacency_list.keys()) + [item for sublist in self.adjacency_list.values() for item in sublist]))
        self.vertex_to_index = {vertex: index for index, vertex in enumerate(self.vertices)}
        self.index_to_vertex = {index: vertex for vertex, index in self.vertex_to_index.items()}
        self.all_edges_list = self.all_edges()
        self.edges_list = self.to_edge_list()
        self.incidence_matrix = self.to_incidence_matrix()
        self.adjacency_matrix = self.to_adjacency_matrix()

    def to_edge_list(self):
        edge_list = []
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                edge_list.append((vertex, neighbor))
        return edge_list

    def to_incidence_matrix(self):
        num_vertices = len(self.vertices)
        # num_edges = len(self.all_edges_list)
        num_edges = len(self.edges_list)
        incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]
        edge_index = 0

        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                incidence_matrix[self.vertex_to_index[vertex]][edge_index] = 1
                incidence_matrix[self.vertex_to_index[neighbor]][edge_index] = -1
                if vertex == neighbor:  # Check for loops
                    incidence_matrix[self.vertex_to_index[vertex]][edge_index] = 2
                edge_index += 1

        return incidence_matrix

    def to_adjacency_matrix(self):
        num_vertices = len(self.vertices)
        adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                adjacency_matrix[self.vertex_to_index[vertex]][self.vertex_to_index[neighbor]] = 1

        return adjacency_matrix

    def all_edges(self):
        edges = []
        for vertex in self.adjacency_list:
            for neighbour in self.adjacency_list[vertex]:
                edges.append((vertex, neighbour))
        return edges
