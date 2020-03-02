from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

figure = ['+','-','/','*']
num = int(input())
n = list(map(int, input().split()))
n2 = list(map(int, input().split()))

multi = []
dic = {}
for i in range(len(figure)):
    dic[figure[i]] = n[i]
for key, value in dic.items():
    for k in range(value):
        multi.append(key)
multi.append('')
result = []
for i in range(len(n2)):
    result.append(n2[i])
    result.append(multi[i])

multiresult = []
multiresult.append(list(powerset(multi)))
for i in multiresult:
    for j in range(len(i)):
        print(i[j])
    


