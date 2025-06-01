# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # find peak
        l, r = 1, length - 2 # peak will never be at ends

        while l <= r:
            m = l + (r - l)//2
            left, mid, right = mountainArr.get(m -1), mountainArr.get(m), mountainArr.get(m + 1)

            if left < mid < right: # in left half of mountain array, now go to right
                l = m + 1
            elif left > mid > right: # and vice versa
                r = m - 1
            else: # found peak where left < mid > right
                break
        
        peak = m 

        # search target in left portion - we want min index so searched here first
        l, r = 0, peak

        while l <= r:
            m = l + (r - l)//2
            val = mountainArr.get(m)

            if val == target:
                return m # if found there wont be any other value with same target value as its a mountain array with stricly decreasing and increasing values
            elif target < val:
                r = m - 1
            else:
                l = m + 1
        
        # search target in right portion - see the conditions are changed as this portion is in descending order
        l, r = peak, length - 1

        while l <= r:
            m = l + (r - l)//2
            val = mountainArr.get(m)

            if val == target:
                return m
            elif target < val:
                l = m + 1
            else:
                r = m - 1

        return -1

