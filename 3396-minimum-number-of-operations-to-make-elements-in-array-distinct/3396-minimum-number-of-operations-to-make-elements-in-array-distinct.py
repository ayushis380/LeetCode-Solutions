class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = {}
        length = len(nums)
        ans = 0

        for i in range(length - 1, -1, -1):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]] > 1:
                return (i//3) + 1

        return 0 
                
