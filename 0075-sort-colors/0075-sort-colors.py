class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # For all idx < p0 : nums[idx < p0] = 0
        # curr is an index of elements under consideration

         # For all idx > p2 : nums[idx > p2] = 2

        p0, cur, p2 = 0, 0, len(nums) - 1

        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1 # dont increase cur in this cond as swapped value from end can again be 2
            else:
                cur += 1
            
                
            
        