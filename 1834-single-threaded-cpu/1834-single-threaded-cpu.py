class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
    # (a) We will insert all the currently available tasks in the min-heap.
    # (b) Pick the task with the shortest processing time.
    # (c) Increase the current time by the processing time of the selected task.

        for i, t in enumerate(tasks):
            t.append(i) # sorting will disturb the index position, so add one more value to the t list
        
        tasks.sort(key = lambda x: x[0]) # O(nlogn)
        heap, result = [], [] # minheap to give shortest jobs priority, O(n)
        i, time = 0, tasks[0][0]

        while heap or i < len(tasks):
            # add all tasks first which fit the time condition
            while i < len(tasks) and time >= tasks[i][0]: # all tasks which have enqtime less than current time can be processed
                heapq.heappush(heap, (tasks[i][1], tasks[i][2])) # shortest job first, if same processing time then index is considered
                i += 1
            
            if not heap:
                # reduce the number of iterations in our approach and improve the run-time
                time = tasks[i][0] # cpu is idle and can go to the next enq time eg time = 2 and next task has enqtime of 7, it can jump to it
            else:
                procTime, index = heapq.heappop(heap)
                time += procTime # next time stamp
                result.append(index)
        
        return result
            


