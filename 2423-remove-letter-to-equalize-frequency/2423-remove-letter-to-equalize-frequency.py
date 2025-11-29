class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        bucket = Counter(list(freq.values()))

        if len(bucket) == 1:
            count, howmany = bucket.popitem()
            return count == 1 or howmany == 1 # aabbcc will give 2: 3, but when we remove anything it will disbalance
        
        if len(bucket) == 2:
            (c1, h1), (c2, h2) = bucket.items()
            if c1 > c2:
                c1, c2 = c2, c1
                h1, h2 = h2, h1
            
            if c1 == 1 and h1 == 1: # c1 is smaller and occurs once
                return True
            
            if c2 == c1 + 1 and h2 == 1: # c2 occurs just one more than c1
                return True
        
        return False
            
            