class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # order of elements doesnt matter
        l, r = 0, len(nums)

        while l < r:
            if nums[l] == val:
                nums[l] = nums[r - 1]
                r -= 1 # when no vals are left, r will reach the point from ehere all vals arre stored till end
            else:
                l += 1
        
        return r # r index is from where not required values start, we need length so r is returned