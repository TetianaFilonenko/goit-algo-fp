import heapq


def dijkstra(graph, start):
    # Initialize distances dictionary with infinity for all vertices
    distances = {vertex: float("infinity") for vertex in graph}
    # Distance to the start vertex is 0
    distances[start] = 0
    # Initialize priority queue with the start vertex and distance 0
    priority_queue = [(0, start)]

    while priority_queue:
        # Pop the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded shortest distance, skip this vertex
        if current_distance > distances[current_vertex]:
            continue

        # Iterate over the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                # Update the shortest distance to the neighbor
                distances[neighbor] = distance
                # Push the updated distance and neighbor to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    # Return the dictionary containing the shortest distances to all vertices
    return distances


# Testing
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}

start_vertex = "A"
shortest_paths = dijkstra(graph, start_vertex)
print(shortest_paths)
