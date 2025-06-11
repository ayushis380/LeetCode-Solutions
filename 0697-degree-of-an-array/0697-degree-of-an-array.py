class Solution(object):
    def findShortestSubArray(self, nums):
# for each element x that occurs the maximum number of times, right[x] - left[x] + 1 will be our candidate answer, and we'll take the minimum of those candidates.
        left, right, count = {}, {}, defaultdict(int)
        
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] += 1

        ans = len(nums) # if only 1 value is present 
        degree = max(count.values())
        
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans