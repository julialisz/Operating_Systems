'''Robin Round'''

chart = []

def shiftCL(queue):
    temp = queue[0]
    for i in range(len(queue)-1):
        queue[i] = queue[i+1]
    queue[len(queue)-1] = temp
    return queue

def RR(tq, result, n):
    global chart
    queue = []
    time = 0
    ap = 0 #arrived processes
    rp = 0 #ready processes
    done = 0 #done processes
    q = tq #time quantum
    start = 0
    while(done<n):
        for i in range(ap, n):
            if(time>=result[i][1]):
                queue.append(result[i])
                ap += 1
                rp += 1
        if(rp<1):
            chart.append(0)
            time += 1
            continue
        
        if(start):
            queue = shiftCL(queue)
        
        if(queue[0][2]>0):
            if(queue[0][2]>q):
                for i in range(time, time+q):
                    chart.append(queue[0][0])
                time += q
                queue[0][2] -= q
            else:
                for i in range(time, time+queue[0][2]):
                    chart.append(queue[0][0])
                time += queue[0][2]
                queue[0][2] = 0
                done += 1
                rp -= 1
            start = 1
 

with open("test1.txt", "r") as file:
    result = [[int(x) for x in line.split()] for line in file]

#sorting arrival time
result = sorted(result, key = lambda l:l[1])
print(result)
numOfProc = len(result)

burstTimes = []
for i in range(numOfProc):
    burstTimes.append(result[i][2])

q = int(input("Enter time quantum: "))

RR(q, result, numOfProc)
print(chart)

waitingTime = 0
for i in range(numOfProc):
    waitingTime += max(loc for loc, val in enumerate(chart) if val == (i+1)) + 1 - burstTimes[i-1]
print("Average waiting time is: " + str(waitingTime/numOfProc))

