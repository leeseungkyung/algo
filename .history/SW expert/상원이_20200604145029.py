N, M = map(int, input().split())

arr = [ [] for _ in range(M+1)]
for i in range(N):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

print(arr)