t = int(input())
for test in range(t):


    v, e = map(int, input().split())
    
    arr = [list((map(int, input().split()))) for _ in range(e)]
    start, end = map(int, input().split())
    dic = {}
    stack = []
    result = 0
    for i in range(1,v+1):
        dic[i]=[]

    for i in range(len(arr)):
        dic[arr[i][0]].append(arr[i][1])
    
    visited = [False]*55
    visited[start] = True
    stack.append(start)

    
    while stack:
        for value in dic[start]:
            if visited[value]==False:
                stack.append(value)
                visited[value]=True
                start = value
                if start == end :
                    print(1)
                    break
        else:
            start=stack.pop()
    print('#{} {}'.format(test,result))
