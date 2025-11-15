from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = [] # There can be at most two majority elements which are more than ⌊n/3⌋ times
        ct1, ct2 = 0, 0
        el1, el2 = 0, 1  # el1 and el2 must be different to avoid conflict

        # First pass to find potential candidates
        for num in nums:
            if ct1 == 0 and num != el2: # num != el2 is important as number need to be different
                ct1 = 1
                el1 = num # new candidate for el1 as ct1 was 0
            elif ct2 == 0 and num != el1:
                ct2 = 1
                el2 = num # new candidate for el2 as ct2 was 0
            elif num == el1:
                ct1 += 1
            elif num == el2:
                ct2 += 1
            else: # when num doesnt match both then decrease both counts
                ct1 -= 1
                ct2 -= 1

        # Second pass to verify the counts
        ct1, ct2 = 0, 0
        for num in nums:
            if num == el1:
                ct1 += 1
            elif num == el2:
                ct2 += 1

        minreq = len(nums) // 3 + 1
        if ct1 >= minreq:
            res.append(el1)
        if ct2 >= minreq:
            res.append(el2)

        return res
