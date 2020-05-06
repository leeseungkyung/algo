def find(k, prek, s):
    global minV
    if k == N:
        s = s + brd[prek][0]
        if minV > s:
            minV = s
        return

    elif minV <= s:
        return

    else:
        for i in range(1, N):
            if visited[i] == 0:
                visited[i] = 1
                find(k+1, i, s+brd[prek][i])
                visited[i] = 0
    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    brd = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    visited[0] = 1
    minV = 100000
    find(1, 0, 0)
    print("#%d %d" % (t, minV))