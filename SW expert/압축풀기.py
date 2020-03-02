T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n=int(input())

    arr= []
    for i in range(n):
        a,b = input().split()
        for _ in range(int(b)):
            arr.append(a)
    count = 0
    print('#{}'.format(test_case))
    while count<len(arr):
        
        print(arr[count],end="")
        count+=1
        if count%10==0:
            print()