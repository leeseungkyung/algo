#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

from collections import deque
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        start = q.popleft()
        print(start, end=' ')
        for i in adj[start]:
            if visited[i]==0 :
                q.append(i)

                visited[i]=1



visited = [0 for _ in range(100)]
v, e = map(int, input().split())
arr = list(map(int, input().split()))
adj = {i:[] for i in range(1,v+1)}

for k in range(e):
    s,e = arr[k*2], arr[k*2+1]
    adj[s].append(e)
    adj[e].append(s)
bfs(1)
