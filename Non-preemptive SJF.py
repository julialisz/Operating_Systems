'''Non-preemptive SJF'''

with open("test.txt", "r") as file:
    result = [[int(x) for x in line.split()] for line in file]

#sorting arrival time
result = sorted(result, key = lambda l:l[1])

currentTime = 0
waitingTime = 0
numOfProc = len(result)
print(numOfProc)

for i in range (numOfProc):
    temp = [process for process in result if process[1] <= currentTime]
    temp = sorted(temp, key = lambda l:l[2])
    print(temp[0])
    waitingTime += currentTime - temp[0][1]
    currentTime = currentTime + temp[0][2]
    
    result.remove(temp[0])


print(waitingTime)

averageTime = waitingTime/numOfProc
print("Average waiting time for Non-Preemptive SJF algorithm is " + str(averageTime))
