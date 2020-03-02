T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    

    from itertools import chain, combinations

    n , b = map(int, input().split()) #점원, 선반높이
    h = list(map(int, input().split()))

    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))


    result = list(powerset(h))
    mina = b
    for i in result:
        sum1=0
        for j in range(len(i)):
            sum1+= i[j]
        if sum1>=b:
            if abs(sum1-b)<mina:
                mina = sum1-b
    print('#{}'.format(test_case), mina)

        
