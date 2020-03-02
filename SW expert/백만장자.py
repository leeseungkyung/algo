T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    num = int(input())
    arr = list(map(int, input().split()))
    max_number = arr[-1]
    answer = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] < max_number:
            answer += max_number-arr[i]
        else:
            max_number = arr[i]
    print('#{} {}'.format(test_case, answer))