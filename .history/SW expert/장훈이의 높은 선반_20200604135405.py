from itertools import combinations


T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    result = []

    for k in range(2, N):
        for i in list(combinations(S,k)):
            result.append(i)
    print(result)

    def check():
        
        min_result = 100
        for idx in result :
            if sum(idx)>=B:
                k = sum(idx)-B
                print(k)

    print('#{} {}'.format(test_case, check()))
