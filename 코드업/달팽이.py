a= int(input())
arr = [[0 for _ in range(a)] for _ in range(a)]

i = 0 #i열
j = -1 #j행
count = 0 #배열에 들어가는 숫자
sw= 1 #스위치 변수
p = a #반복문 도는 횟수 
while count<a*a: #배열에 숫자가 다 채워지면 종료 

    for _ in range(p):
        count +=1
        j+=sw
        arr[i][j] = count 
    p = p-1

    
    for _ in range(p):
        count+= 1
        i = i+sw
        arr[i][j] =count 
    sw *= -1

for i in range(a):
    for j in range(a):
        print(arr[i][j], end =' ')
    print()
    


        