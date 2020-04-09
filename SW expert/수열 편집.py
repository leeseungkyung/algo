
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):


    n, m, l = map(int, input().split())

    arr = list(map(int, input().split()))

    def change(arr,a, b, c):
        if a=="I":
            arr.insert(b,c)
        if a=="C":
            arr[b]=c

    def delete(arr,a):
        del(arr[a])

    change_list = [list(input().split()) for _ in range(m)]

    for i in range(len(change_list)):
        if len(change_list[i])==3:
            change(arr, change_list[i][0], int(change_list[i][1]), int(change_list[i][2]))
        else:
            delete(arr, int(change_list[i][1]))

    try:
        result = arr[l]
    except IndexError:
        result = -1

    print('#{} {}'.format(test_case, result))