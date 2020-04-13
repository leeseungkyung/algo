import sys
from collections import deque

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            q.append((i,j,cnt))       

move = [(0,1),(1,0),(-1,0),(0,-1)]

result = 0
def bfs(q, cnt):
    global result
    while q:
        q_x, q_y, cnt = q.popleft()

        for i,j in move :
            dx = q_x+i
            dy = q_y+j

            if 0<= dx < n and 0 <= dy < m and arr[dx][dy]==0:
                arr[dx][dy]= cnt+1
                q.append((dx,dy,cnt+1))
                result = cnt+1

    return result
k = bfs(q,cnt)

for i in arr:
    if 0 in i:
        print(-1)
        exit()
print(k)