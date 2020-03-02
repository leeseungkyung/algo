T = int(input())

for test_case in range(T):
    n = int(input())
    dic = {}
    for i in range(1, 5001):
        dic[str(i)] = 0

    for i in range(n):
        a, b = map(int,input().split())
        arr2 = [i for i in range(a,b+1)]

        for i in arr2:
            dic[str(i)]+=1

    p = int(input())
    result_arr = []
    for i in range(p):
        result = input()
        result_arr.append(dic[result])

    print('#{}'.format(test_case+1), *result_arr)