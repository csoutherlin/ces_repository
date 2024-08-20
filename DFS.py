def dfs(graph, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
       (vertex, path) = stack.pop()
       if vertex not in visited: 
           if vertex == end:
               return path
           visited.add(vertex)
           for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
end_node = 'F'
path = dfs(graph, start_node, end_node)
print(f"Path from {start_node} to {end_node}: {path}")