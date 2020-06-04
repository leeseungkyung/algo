from itertools import permutations
T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

result = []

for k in range(1, B):
    for i in list(permutations(S,k)):
        result.append(i)
print(result)