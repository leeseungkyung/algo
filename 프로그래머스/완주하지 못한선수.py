participant =		["marina", "josipa", "nikola", "vinko", "filipa"]
completion =  ["josipa", "filipa", "marina", "nikola"]
participant.sort()
completion.sort()
print(participant, completion)

arr = {}

for i in completion:
    arr[i] = 0

for j in participant:    
    if j in arr:
        arr[j]+=1
    else:
        result = j
        
for key, value in arr.values():
    if value==2:
        result = j

