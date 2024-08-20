from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    distances = {start: 0}
    predecessors = {start: None}

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor] = distances[vertex] + 1
                predecessors[neighbor] = vertex

    return distances, predecessors

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_vertex = 'A'
print(bfs(graph, start_vertex))
