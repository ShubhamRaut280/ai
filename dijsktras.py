import heapq

def dijkstra(graph, start):
    # Initialize distances from the start vertex to all other vertices as infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue to store vertices with their distances
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # If the current distance is greater than the distance already seen, skip
        if current_distance > distances[current_vertex]:
            continue

        # Visit all neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # If the distance to the neighbor through the current vertex is shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
print("Shortest distances from vertex", start_vertex, ":")
print(dijkstra(graph, start_vertex))
