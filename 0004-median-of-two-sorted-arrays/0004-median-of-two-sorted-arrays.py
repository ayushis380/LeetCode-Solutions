class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total//2
        low, high = 0, len(A) - 1

        while True:
            i = (low + high)//2
            j = half - i -2
            # print("i is - ", i, " j is - ", j)

            Aleft = A[i] if i >=0 else float("-inf")
            Aright = A[i+1] if (i + 1) < len(A) else float("inf")

            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+ 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # odd len
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/ 2
            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1
            