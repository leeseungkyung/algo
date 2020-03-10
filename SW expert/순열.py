arr='abc' 
N = len(arr)


perm = []
visit = [0] * N
for i in range(N):
    perm.append(arr[i]); visit[i]=1
    for j in range(N):
        if visit[j]: continue
        perm.append(arr[j]); visit[j]=1
        
        for k in range(N):
            if visit[k]: continue
            perm.append(arr[k]); visit[k] = 1
            print(perm)
            perm.pop(); visit[k]=0
        perm.pop(); visit[j] =0
    perm.pop(); visit[i] = 0
