def dfs(grafo, nodo_iniziale, visitati=None):
    if visitati is None:
        visitati = set()
    print(nodo_iniziale)  # Puoi fare qualsiasi operazione qui con il nodo visitato
    visitati.add(nodo_iniziale)
    for vicino in grafo[nodo_iniziale]:
        if vicino not in visitati:
            dfs(grafo, vicino, visitati)

# Esempio di utilizzo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(grafo, 'A')
