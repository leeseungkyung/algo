T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):



    arr = [list(map(int, input().split()))  for _ in range(9)]


    def f():
        for i in range(0, 9,3):
            for j in range(0, 9, 3):
                check = []
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if arr[k][l] not in check:
                            check.append(arr[k][l])
                        else:
                            return False

        for i in range(9):
            check=[]
            for j in range(9):
                if arr[i][j] not in check:
                    check.append(arr[i][j])
                else:
                    return False

        for i in range(9):
            check=[]
            for j in range(9):
                if arr[j][i] not in check:
                    check.append(arr[j][i])
                else:
                    return False
        return True

    if f()==False:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, 1))
