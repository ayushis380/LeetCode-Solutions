class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       i = 0
       n = len(nums)
       k %= n

       self.reverse(0, nums, n-1) # full reverse
       self.reverse(0, nums, k-1) # k elements reversed
       self.reverse(k, nums, n-1)# n -k elements from end reversed 

    #    nums.reverse()
    #    nums[:k] = reversed(nums[:k])
    
    def reverse(self, start, nums, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        