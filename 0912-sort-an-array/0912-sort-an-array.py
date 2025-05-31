class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    # Counting sort is a non-comparative sorting algorithm and is useful in situations where the elements in the array have a limited range
    # O(n+k) n is the number of elements in the nums array, and k is the range of value of its elements (minimum value to maximum value)
   
        count = Counter(nums)  # O(n)
        i = 0
        minVal = min(nums)
        maxVal = max(nums)

        for v in range(minVal, maxVal +1):
            while count[v] > 0:
                nums[i] = v
                count[v] -= 1
                i += 1

        return nums