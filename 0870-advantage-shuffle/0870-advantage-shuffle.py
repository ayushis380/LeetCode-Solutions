class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sortedA = sorted(nums1)
        sortedB = sorted(nums2)

        assigned = {b: [] for b in nums2}
        remaining = []
        j = 0

        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)
        
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in nums2]