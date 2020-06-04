from itertools import combinations
T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

result = []

for k in range(1, N):
    for i in list(combinations(S,k)):
        result.append(i)
result 