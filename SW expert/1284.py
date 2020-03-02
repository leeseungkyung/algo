n = int(input())
arr = [2,3,5,7,11]

count2 =0
count3 = 0
count5 = 0
count7 = 0
count11 = 0

for i in arr:
    while True:
        if i%n==0:
            if i==2:
                n= i/n
                count2+=1
            if i==3:
                n= i/n
                count3+=1
            if i==5:
                n= i/n
                count5+=1
            if i==7:
                n= i/n
                count7+=1
            if i==11:
                n= i/n
                count11+=1
        else:
            break
print(count2, count3, count5, count7)