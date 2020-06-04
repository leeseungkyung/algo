N, M = map(int, input().split())

arr = [ [] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

print(arr)