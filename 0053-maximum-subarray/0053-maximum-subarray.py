class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-inf")
        presum = 0
        start = end = 0
        temp_start = 0  # Temporary start index for a new subarray

        for i in range(len(nums)):
            presum += nums[i]

            if presum > maxsum:
                maxsum = presum
                start = temp_start  # Update the start index of the max subarray
                end = i  # Update the end index of the max subarray
            
            # If presum is less than 0, reset it and update temp_start
            if presum < 0:
                presum = 0
                temp_start = i + 1  # Potential start of a new subarray

        # Printing the max subarray and the max sum
        max_subarray = nums[start:end + 1]
        print("Max Sum:", maxsum)
        print("Subarray with Max Sum:", max_subarray)
        
        return maxsum

