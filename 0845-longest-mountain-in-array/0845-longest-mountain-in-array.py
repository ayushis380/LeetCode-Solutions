class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0

        for ind in range(1, len(arr) - 1): # mountain wont be present on last indexes
        # look for peaks and expand them, just like palindrome approach
            if arr[ind - 1] < arr[ind] > arr[ind + 1]: # begin expanding
                l = r = ind

                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                while r + 1 < len(arr) and arr[r] > arr[r+1]:
                    r += 1
                
                res = max(res, r - l + 1)
        
        return res