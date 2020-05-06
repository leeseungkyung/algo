def find(r,c,s):
    global minV
    if r==m-1 and c==m-1:
        if minV > s+arr[r][c]:
            minV = s+arr[r][c]
    else:
        if r+1<m:
            find(r+1, c, s+arr[r][c])
        if c+1<m: 
            find(r,c+1,s+arr[r][c])

t= int(input())


for test_case in range(1, t+1):
    m = int(input())
    arr = [list(map(int,input().split()))for _ in range(m)]

    minV = 100000
    find(0,0,0)
    print('#{} {}'.format,minV)

