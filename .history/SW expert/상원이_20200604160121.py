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
    q.append((v,0))
    result = 0
    count = 0
    while q:
        k, count= q.pop(0)
        if count==2:
            break
        for i in arr[k]:
            if not visited[i]:
                q.append((i, count+1))
                visited[i]=1
                result +=1
                
        
    print(result)



