from collections import defaultdict
def parse_node(x):
    try:
        return int(x)
    except ValueError:
        return x
def dfs(graph, start, visited, path):
    visited[start] = True
    path.append(start)
    for neighbour in graph[start]:
        if not visited.get(neighbour, False):
            dfs(graph, neighbour, visited, path)
    return path
n, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    u, v = input().split()
    u = parse_node(u)
    v = parse_node(v)
    graph[u].append(v)
    graph[v].append(u)
start = next(iter(graph))
visited = {}
path = []
traversed_path = dfs(graph, start, visited, path)
print([str(node) for node in traversed_path])
