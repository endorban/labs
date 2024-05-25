# база 1
def Deikstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current_vertex)
        
        if distances[current_vertex] == float('infinity'):
            break
        
        for neighbor, weight in graph[current_vertex].items():
            alternative_route = distances[current_vertex] + weight
            
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                
    return distances




graph = {
    'A': {'B': 4, 'C': 2, 'D': 3},
    'B': {'A': 4, 'C': 1, 'D': 15, 'F': 56},
    'C': {'A': 2, 'B': 1, 'D': 15, 'F': 14},
    'D': {'A': 3,'B': 5, 'C': 1},
    'F': {'B': 56, 'C': 14}
}

print(Deikstra(graph, 'A'))

# база 3
def Deikstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current_vertex)
        
        if distances[current_vertex] == float('infinity'):
            break
        
        for neighbor, weight in graph[current_vertex].items():
            alternative_route = distances[current_vertex] + weight
            
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                
    return distances




graph = {
    'A': {'B': 4, 'C': 2, 'D': 3},
    'B': {'A': 4, 'C': 1, 'D': 15, 'F': 56},
    'C': {'A': 2, 'B': 1, 'D': 15, 'F': 14},
    'D': {'A': 3,'B': 5, 'C': 1},
    'F': {'B': 56, 'C': 14}
}

print(Deikstra(graph, 'A'))
