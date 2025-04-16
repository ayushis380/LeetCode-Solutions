class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
        right = [[] for _ in range(n+1)]  # Stores conflicting left values indexed by their max right value
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))  # Store the smaller value as a left boundary
        
        ans = 0  # Counts valid subarrays without removing a conflict
        left = [0, 0]  # Stores the two largest left boundaries
        bonus = [0] * (n + 1)  # Bonus subarrays if a conflict is removed
        
        for r in range(1, n + 1):  # Iterate over each position in nums
            for l in right[r]:  # Process conflicts ending at r
                left = max(left, [l, left[0]], [left[0], l])  # Update left boundary tracking
            
            ans += r - left[0]  # Add valid subarrays ending at r
            bonus[left[0]] += left[0] - left[1]  # Calculate potential gain from removing the largest conflict
        
        return ans + max(bonus)  # Return maximum valid subarrays after removing the best conflict
