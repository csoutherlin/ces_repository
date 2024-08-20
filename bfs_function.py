def print_shortest_path(predecessors, start, target):
    path = []
    current = target

    # Traverse the predecessors dictionary from target to start
    while current != start:
        path.append(current)
        current = predecessors[current]

    # Add the start node to the path
    path.append(start)

    # Print the path in reverse order
    print(f"Shortest path from {start} to {target}: {path[::-1]}")

# Example usage:
predecessors = {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'B', 'F': 'C'}
start_node = 'A'
target_node = 'E'
print_shortest_path(predecessors, start_node, target_node)
