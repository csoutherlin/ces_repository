def topological_sort_util(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            topological_sort_util(graph, neighbor, visited, stack)
    stack.append(node)

def topological_sort(graph):
    visited = set()
    stack = []

    # Reverse the graph
    reversed_graph = {node: [] for node in graph}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            reversed_graph[neighbor].append(node)

    for node in reversed_graph:
        if node not in visited:
            topological_sort_util(reversed_graph, node, visited, stack)

    return stack[::-1]