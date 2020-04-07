
import sys
sys.setrecursionlimit(10 ** 6)


t = int(input())

for test in range(t):
    m, n, k = map(int, input().split())

    arr = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        a,b = map(int, input().split())
        arr[b][a] = 1
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    cnt = 0
    def dfs(y,x):
        arr[y][x] = 0
        
        for i, j in move:
            dy = i+y
            dx = j+x

            if 0<=dy<n  and 0<=dx<m and arr[dy][dx]==1:
                dfs(dy,dx)
        return


    for y in range(n):
        for x in range(m):
            if arr[y][x]:
                dfs(y,x)
                cnt+=1
    print(cnt)