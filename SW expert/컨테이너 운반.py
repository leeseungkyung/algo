t= int(input())

for test_case in range(1, t+1):

    n, m = map(int, input().split())
    n_list = list(map(int, input().split())) #화물의 무께 
    m_list = list(map(int, input().split())) #트럭 젂재 용량



    n_list.sort(reverse=True)
    m_list.sort(reverse=True)

    n_idx = 0
    m_idx = 0
    result = 0
    while True :
        if m_idx == len(m_list) or n_idx==len(n_list):
            break
        if n_list[n_idx]<=m_list[m_idx]:
            result += n_list[n_idx]
            n_idx+=1
            m_idx+=1
        else:
            n_idx+=1

    print('#{} {}'.format(test_case,result))
