class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # ans = [0] * 2 * length # creates a space for array - after that only the index assignment can be done. it's important to ensure the index exists within the list's range before modifying it
        ans = [] # append and insert safely add the new element
        
        for i in range(length):
            # ans[i] = nums[i]
            # ans[i+length] = nums[i]
            
            ans.insert(i, nums[i])
            ans.insert(i+length, nums[i])
        
        return ans