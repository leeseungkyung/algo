n, m = map(int, input().split())

arr = [ list(map(int, input().split())) for _ in range(m)]

move = [(1,0),(0,1),(-1,0),(0,-1)]
result = 0
def bfs(q):
    while q:
        x, y = q.pop(0)
        for i, j in move:
            dx = x+i
            dy = y+j
            if 0<=dx<n and 0<=dy<m and arr[dx][dy]==0:
                q.append((dx, dy))
                arr[dx][dy] = 2
                
    return count(arr)

def count(arr):
    global result
    for i in range(n):
        for j in range(m):
            if arr[i][j] ==2:
                result +=1
    return result

q = []
cnt = 0
for i in range(n):
    for j in range(m):          
        if arr[i][j] == 0:
            q.append((i,j))


print(bfs(q))