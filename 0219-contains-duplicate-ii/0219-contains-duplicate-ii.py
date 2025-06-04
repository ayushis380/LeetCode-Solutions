class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() # looking for duplicates in size k + 1 window, eg for k = 1, two values need to be there 
        start = 0

        for end in range(len(nums)):
            if end - start > k: # window should be <= k
                window.remove(nums[start])
                start += 1
            if nums[end] in window: # after adjusting the window, we still have duplicates in that window 
                return True
            
            window.add(nums[end])
        
        return False