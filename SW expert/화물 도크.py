T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    t = [list(map(int, input().split())) for _ in range(N)]

    t.sort(key=lambda x: x[1])  
    cnt = 1
    e = t[0][1]
    for i in range(N):
        if t[i][0] >= e :
            e = t[i][1]
            cnt += 1
    
    print('#{0} {1}'.format(test_case, cnt))