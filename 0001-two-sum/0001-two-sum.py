class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, val in enumerate(nums):
            diff = target - val

            if diff in store:
                return [i, store[diff]]
            
            store[val] = i
        
        return [-1, -1]