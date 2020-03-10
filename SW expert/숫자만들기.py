def multi(n, k,r,a,b,c,d):
    global minV, maxV
    if n==k:
        if maxV<r:
            maxV = r
        if minV>r:
            minV = r
    else:
        if a>0:
            multi(n+1, k, r+num[n], a-1,b,c,d)

        if b>0:
            multi(n+1, k, r-num[n], a,b-1,c,d)
        if c>0:
            multi(n+1, k, r*num[n], a,b,c-1,d)
        if d>0:
            multi(n+1, k, int(r/num[n]), a,b,c,d-1)
        

t= int(input())
for t in range(1, t+1):
    N = int(input())
    a,b,c,d =map(int, input().split()) # 연산자의 개수 
    num = list(map(int, input().split())) #수식에 사용되는 숫자

    minV = 10000000000
    maxV = -10000000000
    multi(1,N, num[0], a,b,c,d )
    print('#{} {}'.format(t, maxV-minV))