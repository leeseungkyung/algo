
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    arr= list(map(int, input().split(' ')))

    max = 0
    min = 10000
    result = 0
    for i in arr:
        if max<i :
            max = i
        if min >i:
            min = i
    arr.remove(max)
    arr.remove(min)

    result = result/ len(arr)
    print('#{} {}'.format(test_case,round(result)))