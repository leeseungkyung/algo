N, M = map(int, input().split())

arr = [ [] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0]*(N+1)
v=1
visited[v]=1
q = []

for i in arr[v]:
    q.append(i)
else: 
    count = 0

while q:
    k = q.pop(0)
    visited[k] = 1
    for i in arr[k]:
        if visited[i]==0:
            count+=1
    
    
print(count)



