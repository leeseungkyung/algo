from itertools import combinations
T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    result = []

    for k in range(2, N):
        for i in list(combinations(S,k)):
            result.append(i)


    min_result = 100
    def check():
        
        global min_result
        for i in result :
            if sum(i)==B:
                return sum(i)
            elif sum(i)>B:
                k = sum(i)-B
                if k < min_result :
                    min_result = k
                else:
                    continue
        return min_result

    print('#{} {}'.format(test_case, check()))
