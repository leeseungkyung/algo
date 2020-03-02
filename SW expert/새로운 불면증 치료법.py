T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr= list(map(int, input().split()))
    dic = {}
    for i in arr:
        dic[i]=0
    
    for i in arr:
        dic[i]+=1
    max_value = 0
    max_list = []
    for key, value in dic.items():
        if value>max_value:
            max_value = value
            max_key = key

    print('#{} {}'.format(n,max_key))
    