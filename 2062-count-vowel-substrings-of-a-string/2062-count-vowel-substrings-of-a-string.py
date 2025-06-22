from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        freq = defaultdict(int)  # Tracks frequency of each vowel in the current window

        for i, ch in enumerate(word):
            if ch in "aeiou":
                # If this is the start of a new vowel-only segment
                if i == 0 or word[i - 1] not in "aeiou":
                    j = jj = i     # jj: start of this vowel segment; j: sliding left pointer
                    freq.clear()   # Reset frequency counter for new segment

                freq[ch] += 1  # Add current vowel to frequency map

                # Shrink from left until the window is invalid (missing a vowel or any freq = 0)
                while len(freq) == 5 and all(freq.values()):
                    freq[word[j]] -= 1
                    j += 1

                # Number of valid substrings ending at i = (j - jj)
                # cuaieuouac = uaieuo is valid and gives 2 vowel substrings= uaieuo and aieuo
                # when next char "u" is added to above two vowel subs, it gives two more, so 4 valid vowel subs
                # reason why we have bwlow result calculation after the len(freq) == 5 match 
                result += j - jj
            # else: skip non-vowels completely

        return result
