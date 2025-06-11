class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
    # time complexity is O(n⋅k) because each elimination cycle involves rotating the queue k−1 times, and this happens n−1 times.
    # O(n) due to the queue storing all n friends initially.
        q = deque()

        for i in range(1, n+1): #fill the queue with friends labeled from 1 to n
            q.append(i)
        
        while len(q) > 1:
# we simulate the process by rotating the queue k-1 times. This action effectively moves the k-th friend to the front of the queue, ready for removal
            for i in range(k -1): # under next k friends, the present friend is also included
                q.append(q.popleft()) # add back
            
            q.popleft() # remove kth
        
        return q[0]