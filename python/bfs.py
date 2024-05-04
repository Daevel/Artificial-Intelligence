from collections import deque

def bfs(grafo, nodo_iniziale):
    visitati = set()
    coda = deque([nodo_iniziale])
    
    while coda:
        nodo = coda.popleft()
        if nodo not in visitati:
            print(nodo)  # Puoi fare qualsiasi operazione qui con il nodo visitato
            visitati.add(nodo)
            for vicino in grafo[nodo]:
                if vicino not in visitati and vicino not in coda:
                    coda.append(vicino)

# Esempio di utilizzo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(grafo, 'A')
