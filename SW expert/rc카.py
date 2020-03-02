T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [ [0 for _ in range(N)] for _ in range(N)]

    def aa():

        
        count = 1
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        dist = N-1
        x=0
        y=0
        if dist==0:
            dist= 1
        
        while count <= N*N:
        
            for n in range(4):
                for _ in range(dist):
                    arr[x][y] = count
                    x += dx[n]
                    y +=dy[n]
                    count+=1
                    if count>N*N:
                        return 
            dist -=2
            x = x+1
            y = y+1
            if dist==0:
                dist= 1

    aa()        
    print('#{}'.format(test_case))

    for i in arr:
        for j in range(len(i)):
            print(i[j],end=" ")
        print()


