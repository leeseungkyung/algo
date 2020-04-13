
n, m = map(int, input().split())

arr= [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


move = [(0,1),(1,0),(-1,0),(0,-1)]

q = []
cnt = 1
q.append((0,0,cnt))

def bfs(q, cnt):

    while q:
        x, y, cnt = q.pop(0)
        for i, j in move:
            dx = i+x
            dy = y+j
            if 0<=dx<n and 0<=dy<m and arr[dx][dy]==1 and visited[dx][dy]==0:
                visited[dx][dy] = cnt+1
                q.append((dx,dy, cnt+1))
bfs(q,cnt)
print(visited[-1][-1])