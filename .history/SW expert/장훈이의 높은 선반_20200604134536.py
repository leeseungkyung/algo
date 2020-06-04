from itertools import combinations
T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    result = []

    for k in range(1, N):
        for i in list(combinations(S,k)):
            result.append(i)


    min_result = 100
    for i in result:
        if sum(i)>=B:
            print(sum(i))

    print('#{} {}'.format(test_case, check()))
