T = int(input())

for test_case in range(1, T+1):

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

    count = 0
    result = 0 
    for i in arr[v]:
        q.append((i,1))

    while q:        
        k, j = q.pop(0)
        if j==2: break
        for n in arr[k]:
            if visited[n]==0:
                visited[n]=1
                q.append((n,j+1))
                result +=1 
        
        
    print('#{} {}'.format(test_case,result))



