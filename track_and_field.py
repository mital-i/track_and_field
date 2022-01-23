n = int(input())
graph = {}
times = {}
for i in range(n): 
    line = [int(i) for i in input().split()]
    times[i+1] = line[0]
    graph[i+1] = line[2:]
        
#print(graph, times)

# we create a heap (a data structure which returns the smallest element in O(1))
# In this heap we add (completion time, runner_number)

# eventually we will return the completion time of final runner
import heapq

visited = set(())
h = []
heapq.heappush(h, (times[1], 1))
visited.add(1)


time = 0
while h:
    t, n = heapq.heappop(h)
    time = t
    #print(n)
    #print(graph[n])
    for m in graph[n]:
        if m not in visited:
            heapq.heappush(h, (t + times[m], m))
            visited.add(m)


print(time)
