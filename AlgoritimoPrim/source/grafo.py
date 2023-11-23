import networkx as nx
import random

class Grafo:
    def __init__(self, num_nodes):
        self.G = nx.connected_watts_strogatz_graph(num_nodes, 4, 0.3, seed=42)

        for u, v in self.G.edges():
            self.G[u][v]['distance'] = random.randint(1, 10)
            self.G[u][v]['installation_cost'] = random.randint(1, 5)

    # Métodos da classe...
