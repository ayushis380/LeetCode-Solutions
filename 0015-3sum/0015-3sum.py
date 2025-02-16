class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        self.result = []

        for i in range(length):
            if i == 0 or nums[i] != nums[i-1]:
                self.twosum(nums, i)
        
        return self.result

    def twosum(self, nums, i):
        val = nums[i]
        low, high = i + 1, len(nums) - 1

        while low < high:
            total = val + nums[low] + nums[high]
            if total == 0:
                self.result.append([nums[i], nums[low], nums[high]])
                low += 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
            elif total > 0:
                high -= 1
            else:
                low += 1
