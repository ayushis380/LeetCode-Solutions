class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
    # Binary Search = O(n * log S) = S is sum of nums, range can be from 1 to sum(nums)
    
        low, high = max(nums), sum(nums) # if k = len of nums then min largest sum will be the max of nums, so low has that value
        minLargestSum = high

        while low <= high:
            midSum = low + (high - low) //2
            total = 0
            kpossible = 1

            for n in nums:
                if total + n > midSum:
                    kpossible += 1
                    total = 0
                
                total += n
            
            if kpossible > k:
                low = midSum + 1
    # when kpossible <= k, it means we can just split nums into more subarrays to achieve k number of sub arrays, as even after splitting the sum would remain lower than midSum
            else: 
                minLargestSum = min(minLargestSum, midSum)
                high = midSum - 1

        
        return minLargestSum
            

