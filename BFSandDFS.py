from collections import deque

graph = [[] for _ in range(5)]

graph[0].extend([1, 2])
graph[1].append(2)
graph[2].append(3)
graph[3].append(4)
graph[2].append(0)
graph[1].append(0)
graph[3].append(2)
graph[4].append(3)

def dfs(node, visited):
    visited[node] = True
    print(node, end=" ")
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

def bfs(start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

print("DFS:", end=" ")
visited = [False] * len(graph)
dfs(0, visited)

print("\nBFS:", end=" ")
bfs(0)
