class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # each operation, it changes all the minimum non-zero numbers to 0, that's to say - the number of operations is the number of unique non-zero elements in the array.

        return len(set(nums) - {0})

