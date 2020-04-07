n = int(input())

arr = [list(input()) for _ in range(n)]

move = [(0,1),(1,0),(-1,0),(0,-1)]
cnt = 0
result = 0
def dfs(y,x):
    global result 
    arr[y][x] = 0
    
    result+=1
    for i,j in move:
        dy = i+y
        dx = j+x
        
        if  0<=dy<n and 0<= dx <n and int(arr[dy][dx]):
            dfs(dy,dx)
    return

result_arr = []
for i in range(n):
    for j in range(n):
        result = 0
        if int(arr[i][j]):
            cnt+=1
            dfs(i,j)
            
    
            result_arr.append(result)
print(cnt)
result_arr.sort()

for i in result_arr:
    print(i)