import collections
n= int(input())
m = int(input())

node = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
def bfs(k):
    q = collections.deque()
    q.append(k)
    visited[k] = True
    cnt = 0
    while q:
        v = q.popleft()
        for i in node[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                print(i)
    return cnt


for i in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

print(bfs(1))

