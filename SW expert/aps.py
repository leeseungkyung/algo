arr= [1,2,3,4,5] ; n = len(arr)

for i in range(0, n-3+1):
    for j in range(i+1, n-2+1):
        print(arr[:i+1], end="")
        print(arr[i+1: j+1], end="")
        print(arr[j+1:n], end="")