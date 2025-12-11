class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        bucket = Counter(count.values())

        if len(bucket) == 1:
            ct, frq = bucket.popitem()
            return ct == 1 or frq == 1
        
        # print(bucket)
        if len(bucket) == 2:
            c1, f1 = bucket.popitem()
            c2, f2 = bucket.popitem()

            if c1 > c2:
                c1, c2 = c2, c1
                f1, f2 = f2, f1
            
            if c1 == 1 and f1 == 1:
                return True
            elif c2 == c1 + 1 and f2 == 1:
                return True
        
        return False