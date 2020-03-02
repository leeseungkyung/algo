
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())
    sosu = [2,3,5,7,11]
    arr = []



    while n>True:

        for j in sosu:
            if n%j==0:
                arr.append(j)
                n=int(n/j)
            else:
                continue
        if n==1 or n==0:
            break

    dic = {}
    for i in sosu:
        dic[i]=0
    for i in arr:
        dic[i]+=1

    result= []
    for value in dic.values():
        result.append(str(value))

    result = ' '.join(result)
    print('#{} {}'.format(test_case, result))