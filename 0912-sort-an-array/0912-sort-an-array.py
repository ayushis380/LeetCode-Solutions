class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        minv, maxv = min(nums), max(nums)
        i = 0

        for val in range(minv, maxv + 1):
            while count[val] > 0:
                nums[i] = val
                count[val] -= 1
                i += 1
        
        return nums