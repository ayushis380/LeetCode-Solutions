class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m-1, n-1
        
        for p in range(m + n -1, -1, -1):
            if p2 < 0: # there are no elements left in nums2, and the merging process can stop.
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else: # when p1 < 0 (no elements left in nums1) or nums2[p2] >= nums1[p1].
                nums1[p] = nums2[p2]
                p2 -= 1
        