m, n, x, y = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(n)]
max_arr = 0 
result_arr = []
for i in range(n-y+1):
    for j in range(m-x+1):
        result = 0 
        for k in range(i,i+y):
            for l in range(j, j+x):
                result += arr[k][l]
        result_arr.append(result)
print(max(result_arr))