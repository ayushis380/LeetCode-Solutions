class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 # pick 0 as it wont cause cycle

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        nslow = 0
        while slow != nslow:
            slow = nums[slow]
            nslow = nums[nslow]
        
        return nslow
