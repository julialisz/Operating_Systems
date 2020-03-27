'''Preemptive SJF'''
        
def findavgTime(result, numOfProc):  
    waitingTime = [0] * numOfProc
    tat = [0] * numOfProc  
  
    # Find waiting time of all processes  
    time = 0
    complete = 0
    minm = 99999
    short = 0
    check = False
    rt = [0] * numOfProc #remaining time
    # Copy the burst time into rt[]  
    for i in range(numOfProc):  
        rt[i] = result[i][2]
    
    while(complete!=numOfProc):
        for j in range(numOfProc):
            if((result[j][1]<=time) and (rt[j]>0)):
                minm = rt[j]
                short = j
                check = True
        if(check == False):
            time += 1
            continue
        rt[short] -=1
        minm = rt[short]
        if(minm==0):
            minm=99999
        if(rt[short]==0):
            complete += 1
            check = False
            fintime = time+1  #find finish time of current
            waitingTime[short] = (fintime - result[short][1] - result[short][2]) 
            if(waitingTime[short]<0):
                waitingTime[short]=0
        time += 1 
  
    for i in range(numOfProc): 
        tat[i] = result[i][2] + waitingTime[i]  
  
    total_wt = 0
    total_tat = 0
    for i in range(numOfProc): 
  
        total_wt = total_wt + waitingTime[i]  
        total_tat = total_tat + tat[i]  
    
    averageWT = total_wt/numOfProc
    print(total_wt)
    print("Average waiting time is: " + str(averageWT))


with open("test.txt", "r") as file:
    result = [[int(x) for x in line.split()] for line in file]

#sorting arrival time
result = sorted(result, key = lambda l: (l[1], l[2]))
numOfProc = len(result)
findavgTime(result, numOfProc)