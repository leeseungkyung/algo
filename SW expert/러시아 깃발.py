n, m = map(int, input().split())
arr = [ list(input()) for _ in range(n)]


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()