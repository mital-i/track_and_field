n = int(input())
runners = {}

for i in range(n): 
    runner_i = [int(i) for i in input().split()]
    runners[i+1]=runner_i
    
for i in list(runners.keys()): 
    print(i, runners[i])
    
print()
tracker = [0]*n
end_time = 0
def find_end_time(n, runners, current_runner, curr_max_time, current_time, tracker): 
    global end_time
    print(current_runner)
    if tracker[current_runner-1]!=0:
        curr_max_time = max(current_time, end_time)
        end_time = curr_max_time
        print(current_time, end_time, curr_max_time)
        return
    
    current_time+=runners[current_runner][0]
    tracker[current_runner-1]+=1
    if runners[current_runner][1] == 0: 
        curr_max_time = max(current_time, end_time)
        end_time = curr_max_time
        print(current_time, end_time, curr_max_time)
        return
    print(current_runner, current_time)
    for i in runners[current_runner][1:]: 
        find_end_time(n, runners, i, curr_max_time, current_time, tracker)

find_end_time(n, runners, 1, 0, 0, tracker)
print(end_time)
