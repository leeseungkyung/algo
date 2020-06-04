N, M = map(int, input().split())

arr = [ [] for _ in range(M+1)]
for i in range(M):
    a, b = map(int, input())
    arr[a].append(b)
    arr[b].append(a)

print(arr)