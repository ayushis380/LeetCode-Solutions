class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: # strictly less than k, if k = 1 then no elements as nums starts from 1
            return 0
        
        count, product = 0, 1
        start = 0

        for end, num in enumerate(nums):
            product *= num
            
# Shrink the window from the left while the product is greater than or equal to k
            while product >= k:
                product //= nums[start]
                start += 1

# Update the total count by adding the number of valid subarrays with the current window size
            count += end - start + 1 # right - left + 1 represents the current window size
        
        return count 

# Consider an example window containing elements 3, 4, and 5. If we include 6 in the window, we need to count all possible subarrays that end with 6. These subarrays can be formed by starting at any element within the current window and extending to 6. Therefore, the subarrays would be:

# [6] (subarray consisting only of 6)
# [5, 6] (subarray starting from 5 and ending at 6)
# [4, 5, 6] (subarray starting from 4 and ending at 6)
# [3, 4, 5, 6] (subarray starting from 3 and ending at 6)

# By calculating right - left + 1, we enumerate all subarrays that end with the current element of the window (nums[right])