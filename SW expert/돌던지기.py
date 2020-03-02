
import sys


sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    result = []
    N, K = map(int, input().split())
    for i in range(N):
        a,b,c = map(int, input().split())
        result.append(a*0.35+b*0.45+c*0.2)

    result_score=result[K-1]
    result.sort()
    grade.reverse()
    idx = result.index(result_score) // (N//10)
    n/10
    result_grade = grade[idx]
    print('#{} {}'.format(test_case, result_grade))