n = int(input())
arr = [list(input()) for _ in range(n)]
s= e = n//2
result = 0 
for i in range(n):
    for j in range(s,e+1):
        result+= int(arr[i][j])
    if i< n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(result)
