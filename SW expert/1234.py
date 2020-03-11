

T =10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length, number = input().split()
    numbers = list(number)

    i=0
    while True:
        
        for i in range(len(numbers)-1):
            if numbers[i]==numbers[i+1]:
                for j in range(2):
                    del numbers[i]
                i=0
                break
        else:
            break
        
    print('#{}'.format(test_case), end=" ")
            
    for i in numbers:
        for j in range(len(i)):
            print(i[j],end="")
    print()
