from collections import deque

def bfs(graph, start):

    visited = []
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

if __name__ == "__main__":

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }   

    start = 'A'

    print("BFS traversal:", bfs(graph, start))     