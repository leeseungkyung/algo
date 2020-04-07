n, m = map(int, input().split())
arr = [ list(input()) for _ in range(n)]


for i in range(n-3+1):
    for k in range(i+1, n-2+1):
        for l in range(i+k):
            for j in range(m):
                print(arr[l][j], end="")
            print()
            print()