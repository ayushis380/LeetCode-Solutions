class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 # think indexes of nums as nodes, 0 will never be in cycle as nums values lie from 1 to n 

        # find intersection point of fast and slow
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Floyd algo 
        # find the start of cycle by taking a second slow pointer
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow