class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0 # do not check on n == 0 as it will fail if n = 0 is passed in test case

        for i in range(length):
            if flowerbed[i] == 0:
                # Check if left and right positions are empty
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1 # to check how many flowers can be placed
                    if count >= n:
                        return True  # return early

        return count >= n
