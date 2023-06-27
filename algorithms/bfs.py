from collections import deque

def bfs(graph, start):
    visited = set()              # Set to track visited vertices
    queue = deque([start])       # Queue to store vertices to visit
    
    while queue:
        vertex = queue.popleft()    # Dequeue a vertex from the queue
        if vertex not in visited:
            print(vertex)           # Process the vertex (you can perform any operation here)
            visited.add(vertex)     # Mark the vertex as visited

            # Enqueue all unvisited neighboring vertices
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
