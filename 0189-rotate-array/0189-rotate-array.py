class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k %= length # within bound

        start, count = 0, 0
        # cyclic replacement
    # start at 0, now 0 % k = 0, in each iter all indexes with i % k = 0 will be placed correctly
    # then start is increased and set for all other indexes
        while count < length:
            current, prev = start, nums[start]
            while True:
                new_idx = (current + k) % length # new index 
                nums[new_idx], prev = prev, nums[new_idx] # swap with previous value
                current = new_idx # go to new index
                count += 1 # only swaps required = length

                if current == start: # reached from where we started
                    break
            
            start += 1 # go to next index and place values