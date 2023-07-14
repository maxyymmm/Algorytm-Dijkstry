def dijkstra(G, w, s):
    # Tworzenie słowników
    distance = {v: float('inf') for v in G}
    predecessor  = {v: None for v in G}
    distance[s] = 0

    # Lista wierzchołków
    Q = {v for v in G}

    while Q:
        u = min(Q, key=lambda v: distance[v]) # Wierzchołek z najmniejszą odległością
        Q.remove(u)

        for v in G[u]:
            new_distance = distance[u] + w[(u, v)] # Nowa odległość
            if new_distance < distance[v]:
                distance[v] = new_distance # Przypisanie nowej odległości
                predecessor [v] = u # Poprzednik wierzchołka

    return distance, predecessor 
if __name__ == "__main__":
    G = {'A': ['B', 'E'], 'B': ['C', 'E'], 'C': ['D'], 'D': ['C', 'A'], 'E': ['C', 'B', 'D']} # G(V,E) Klucz: wirzchołek(V=vertex), wartość: krawędź (E=edge)
    w = {('A', 'B'): 10, ('A', 'E'): 5, ('B', 'C'): 1, ('B', 'E'): 2, ('C', 'D'): 4, ('D', 'C'): 6, ('D', 'A'): 7, ('E', 'D'): 2, ('E', 'C'): 9, ('E', 'B'): 3}
    s = 'A'

    distance, predecessor  = dijkstra(G, w, s)

    print(distance)
    print(predecessor)  