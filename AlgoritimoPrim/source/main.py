from grafo import Grafo
from prim import prim
import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Criando um grafo
    grafo = Grafo(20)

    # Exibindo o grafo
    pos = nx.spring_layout(grafo.G)
    nx.draw(grafo.G, pos, with_labels=True, font_weight='bold')
    edge_labels = {(u, v): f"Dist: {grafo.G[u][v]['distance']}, Cost: {grafo.G[u][v]['installation_cost']}" for u, v in grafo.G.edges()}
    nx.draw_networkx_edge_labels(grafo.G, pos, edge_labels=edge_labels)
    plt.show()

    # Aplicando o algoritmo de Prim
    minimum_spanning_tree = prim(grafo.G)

    # Exibindo a Árvore Geradora Mínima
    T = nx.Graph()
    T.add_edges_from([(u, v, {'distance': d}) for u, v, d in minimum_spanning_tree])

    pos_T = nx.spring_layout(T)
    nx.draw(T, pos_T, with_labels=True, font_weight='bold')
    edge_labels_T = {(u, v): f"Dist: {T[u][v]['distance']}" for u, v in T.edges()}
    nx.draw_networkx_edge_labels(T, pos_T, edge_labels=edge_labels_T)
    plt.title("Árvore Geradora Mínima (Prim)")
    plt.show()

if __name__ == "__main__":
    main()
