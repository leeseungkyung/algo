arr = [list(map(int, input().split())) for i in range(10)] #보드판 정보 입력 
result = list(map(int, input().split()))  #말의 위치

    
for i in range(10):
    if result[i]==1: #말이 1일때 
        for j in range(9,-1,-1): #위로 올라감 
            if arr[j][i] > 0:  #올라가다 0보다 큰 숫자가 있으면 
                res = 'crash' #res에 crash를 담아주고 break
                break
            elif arr[j][i]<0:
                res = 'fall'
                break
            else:
                res = 'safe' 
        print(i+1, res)
