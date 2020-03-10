T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    case = list(input())
    h = int(input())
    a = list(map(int, input().split()))

    a=sorted(a, reverse=True)

    for i in a:
        case.insert(i, '-')

    print(case)