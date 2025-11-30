class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
    # nums[i]+nums[j]>nums[k] for the triplet (nums[i],nums[j],nums[k]) to form a valid triangle
        count = 0
        nums.sort() # if we sort them we dont have to check all the inequalties of i, j, k
        n = len(nums)
# 2 5 6 7 9, when n[i] = 5, n[j] = 6, n[k] = 7, 9 satisfies
# when j is increased n[i] = 5, n[j] = 7, then all old n[k] will also satisfy as they are in sorted order
        for i in range(n -2):
            k = i + 2
            for j in range(i+1, n-1):
                if nums[i] != 0:
                    while k < n and nums[i] + nums[j] > nums[k]:
                        k += 1 # reason we dont update k for all the j values in one iter
            # count of elements satisfying the inequality will be given by (k−1)−(j+1)+1=k−j−1
                    count += k - j - 1 
        
        return count