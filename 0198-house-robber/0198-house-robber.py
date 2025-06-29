class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        arr = []

        for i in range(len(nums)):
            tmp = prev2 + nums[i]
            prev2 = prev1
            prev1 = max(tmp, prev1)
            arr.append(prev1)
        
        print(arr)
        return prev1