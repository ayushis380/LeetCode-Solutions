class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for n in nums:
            if n in store:
                return True
            
            store.add(n)
        
        return False