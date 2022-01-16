n = int(input())
runners = {}

for i in range(n): 
    runner_i = [int(i) for i in input().split()]
    runners[i+1]=runner_i
    
tracker = [0]*n
end_time = 0
def find_end_time(n, runners, current_runner, curr_max_time, current_time, tracker): 
    global end_time
    #print(current_runner)
    if tracker[current_runner-1]!=0:
        curr_max_time.append(current_time)
        #end_time = curr_max_time
        return
    
    current_time+=runners[current_runner][0]
    curr_max_time[0] = max(current_time, curr_max_time[0])
    tracker[current_runner-1]+=1
    
    if (current_runner == n): 
        curr_max_time[0] = max(current_time, curr_max_time[0])
        return 
        
    if runners[current_runner][1] == 0: 
        curr_max_time[0] = max(current_time, curr_max_time[0])
        #end_time = curr_max_time
        return
    
    for i in runners[current_runner][1:]: 
        if (tracker[i-1]!=1): 
            find_end_time(n, runners, i, curr_max_time, current_time, tracker)

curr_max = [0]
find_end_time(n, runners, 1, curr_max, 0, tracker)
print(curr_max[0])




q = heap()
q.push(2, 1) 
while(!q.empty()):
    node = q.pop()
    if(visited[node]):
        continue
    
    
    
    
    
    for(next in runners[node]):
        q.push(next)
