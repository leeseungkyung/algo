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
    
        

print(*numbers)