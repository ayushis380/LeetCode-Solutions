class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # O(n - k) — because we shrink the window n - k times (each time either l or r moves).
# The array is sorted, which allows us to safely trim the farthest elements from both ends without missing any possible closer elements in between.
# We're always removing the element that's less optimal (farther from x, or larger in case of a tie).
# Once the window is size k, the elements inside are the best possible choice.

        left, right = 0, len(arr) - 1

        while right - left >= k:
            if abs(x - arr[left]) <= abs(x - arr[right]): # equal cond to right as its sorted as left value is given priority 
                right -= 1
            else:
                left += 1
        
        return arr[left: right + 1]