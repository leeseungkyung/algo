T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    i = int(input())
    arr = list(map(int, input().split()))

    arr2 = []

    while len(arr):
        a = max(arr)
        b = min(arr)
        arr2.append(str(a))
        arr2.append(str(b))
    
        arr.remove(a)
        arr.remove(b)
    print('#{}'.format(test_case),*arr2[:10])
    