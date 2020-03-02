n,m = map(int(input().split())
arr = [list(map(int, input().split())) for i range(n)]

a = []

for j in range(len(arr)):
    for i in range(1,len(arr)+1):
        result = arr[j][0:i]
        a.append(result)