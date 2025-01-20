class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # finding a value val, for which outlier = total - 2 * val 
        # total = sum of n-2 elem + sum + outlier
    
    # eg [2,3,5,10] here when val = 5 we can find the outlier 
    # as it satisfies the cond
        total_sum = sum(nums)
        outlier = float("-inf")

        count = Counter(nums)

        for val in nums:
            potential_outlier = total_sum - 2 * val
    
    # [1,1,1,1,1,5,5] here val and outlier are same
    # so the count is also greater than 1 
            if potential_outlier in count:
                if potential_outlier != val or count[val] > 1:
                    outlier = max(outlier, potential_outlier)
        
        return outlier