# Graphs Data Structure
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:  # If the value exist in the list
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:  # value doesn't exist in list, do nothing
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            # self.adj_list.pop(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def __repr__(self):
        vertex_list = []
        for key, value in self.adj_list.items():
            word = f"{key}: {value}"
            vertex_list.append(word)
        return '\n'.join(vertex_list)


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge("A", 'B')
my_graph.add_edge("A", 'C')
my_graph.add_edge("A", 'D')
my_graph.add_edge("B", 'D')
my_graph.add_edge("C", 'D')

# my_graph.remove_edge('A', 'D')
my_graph.remove_vertex('D')
print(my_graph)
