# a = 10
# # 2의 n승 , 왼쪽 쉬프트
# print(a<<1)
# print(1<<1)
# print(1<<2)
# print(1<<3)

# #오른쪽 쉬프트는 n//2
# print(20>>1)
# print(21>>1)


# #마지막 비트값 : and연산을 통해 알 수 있다.
# if 6 & 1:
#     print('홀수')
# else:
#     print('짝수')


arr = [3,4,5,6,7,8]
n = len(arr)

for i in range(1<<n):
    for j in range(n+1):
        if i& (i<<j):
            print(arr[j], end = " ")
    print()
print()