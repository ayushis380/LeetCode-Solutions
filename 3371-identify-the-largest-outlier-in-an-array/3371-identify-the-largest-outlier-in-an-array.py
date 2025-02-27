class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        outlier = float("-inf")
        count = Counter(nums)

        for val in nums:
            potential = total - 2 * val

            if potential in count:
                if potential != val or count[val] > 1:
                    outlier = max(outlier, potential)
        
        return outlier

