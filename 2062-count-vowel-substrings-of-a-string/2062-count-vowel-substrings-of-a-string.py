class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        freq = defaultdict(int)
        start = 0

        for i, ch in enumerate(word):
            if ch in "aeiou":
                if i == 0 or word[i-1] not in "aeiou":
                    j = jj = i
                    print("window started at ", jj)
                    freq.clear()
                
                freq[ch] += 1

                while len(freq) == 5 and all(freq.values()):
                    freq[word[j]] -= 1
                    j += 1
                
                print("j ends at ", j)
                result += j - jj # j is like looking for an index within a vowel substring where the substring from j to end is also a vowel substring 
        
        return result