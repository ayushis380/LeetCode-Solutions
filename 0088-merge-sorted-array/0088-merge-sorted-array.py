class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = 0, 0
        p3 = m 

        while p1 < (m + n) and p2 < n:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                nums1[p1] = nums2[p2]
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                p1 += 1
        
        while p2 < n:
            nums1[p3] = nums2[p2]
            p2 += 1
            p3 += 1
        