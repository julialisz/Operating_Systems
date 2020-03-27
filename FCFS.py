'''FCFS'''
with open("test.txt", "r") as file:
    result = [[int(x) for x in line.split()] for line in file]
    
result = sorted(result, key = lambda l:l[1])

waitingTime = 0
currentTime = 0

for i in range(1, len(result)):
    waitingTime = waitingTime + currentTime + result[i][1]
    currentTime += result[i][2]
    
for record in result: 
    print(record)
    
print(waitingTime)

averageTime = waitingTime/len(result)

print("Average time for FCFS algorithm is " + str(averageTime))
