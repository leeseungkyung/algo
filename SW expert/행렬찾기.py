
import sys


sys.stdin = open("input (14).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
   
    count = 0
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]>0:
                count+=1
            if arr[i][j]==0 and count >0:
                result.append(count)
                count = 0
            if j==len(arr)-1 and count>0:
                result.append(count)
                count = 0

    dic = {}
    for i in result:
        dic[i] = 0
    for i in result:
        dic[i]+=1
    
    arr_result = []
    for key, value in dic.items():
        arr_result.append([value,key, value*key])

    print('#{}'.format(test_case),len(arr_result), end=" ")

    result_sort = sorted(arr_result, key = lambda x:x[2])
    
    for i in range(len(result_sort)):
        print(result_sort[i][0], result_sort[i][1], end = " ")
    print()