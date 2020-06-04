from itertools import combinations
T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

result = []

for i in list(combinations(S,2)):
    result.append(i)
print(result)