class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1

        while low < high:
            val = numbers[low] + numbers[high]

            if val == target:
                return [low +1, high +1]
            elif val > target:
                high -= 1
            else:
                low += 1
        