# x:행 , y:열
# 상, 하, 좌, 우

dx = [-1, 1, 0,0]
dy = [0,0. -1, 1]

arr = [[]]

for x in range(N):
    for y in range(N):
        for i in range(4):
            tx, ty = x+dx[i], y+dy[i]
            #항상 경계 체크 필요
            if 0<=tx <N and 0 <= ty < N:
                #tx, ty에 대해 작업을 한다. 