class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k %= length

        start, count = 0, 0

# the total count of numbers exclusive numbers placed at their correct position will be k× n / k = n

        while count < length: 
            current_idx, prev_val = start, nums[start]
            while True:
                new_idx = (current_idx + k) % length
        # place the old value at new index and keep copy of this index value for next iteration
                nums[new_idx], prev_val = prev_val, nums[new_idx] 
                # print("new state of nums: ", nums)
                current_idx = new_idx
                count += 1

                if current_idx == start: # means placed all values at required position for this value of start 
                    break
            
            start += 1

# [1,2,3,4,5,6] k = 2
# new state of nums:  [1, 2, 1, 4, 5, 6]
# new state of nums:  [1, 2, 1, 4, 3, 6]
# new state of nums:  [5, 2, 1, 4, 3, 6]
# new state of nums:  [5, 2, 1, 2, 3, 6]
# new state of nums:  [5, 2, 1, 2, 3, 4]
# new state of nums:  [5, 6, 1, 2, 3, 4]