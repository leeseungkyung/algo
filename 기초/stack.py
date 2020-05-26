def dfs(v):
    visited[v]r= 1
    print(v, end=' ')
    for i in range(1, V+1):
        if adj[v][i] == 1 and visited[i] == 0:
            dfs(i)

V, E = map(int, input().split())
edges = list(map(int, input().split()))

adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    s, e = edges[2*i], edges[2*i+1]
    adj[s][e] = 1
    adj[e][s] = 1

visited = [0] * (V+1)
dfs(1)