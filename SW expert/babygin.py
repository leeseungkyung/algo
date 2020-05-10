player1 = [] # 홀수
player2 = [] # 짝수

# 3개일때 
# 정렬 하고... 연속인지 확인
# 같은숫자인지 확인
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if i%2: # 홀수면
        player1.append(arr[i])
    else:
        player2.append(arr[i])

print(player1)
def check(play):
    play.sort()
    idx = 0
    a = play[idx]
    count = 1
    while idx < len(play)-1:
        idx+=1
        if a == play[idx]:
            count+=1
            if count>=3:
                return "triplet"
        else:
            count = 1
            a = play[idx]
    else:
        start = 0
        end = 2
        play.sort()
        while end!= len(play):
            if play[start]+1 == play[start+1]:
                if play[start+1]+1 == play[end]:
                    return 'run'
                else:
                    start+=1
                    end+=1
            else:
                start+=1
                end+=1
    return 0


print(check(player2))
print(check(player1))
# def check2(play):
#     start = 0
#     end = 2
#     play.sort()
#     while end!= len(play):
#         if play[start]+1 == play[start+1]:
#             if play[start+1]+1 == play[end]:
#                 return 'run'
#             else:
#                 start+=1
#                 end+=1
#         else:
#             start+=1
#             end+=1
#     return 0


