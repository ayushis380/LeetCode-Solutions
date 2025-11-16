class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minv, maxv = min(nums), max(nums)
        count = Counter(nums)
        result = []

        for val in range(minv, maxv + 1):
            if val in count:
                while count[val]:
                    result.append(val)
                    count[val] -= 1
        
        return result

