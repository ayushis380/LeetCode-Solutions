class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Frequency count of characters in s1
        s1_count = Counter(s1)
        window_size = len(s1)
        window_count = Counter()

        for i in range(len(s2)):
            # Add the current character to the window
            window_count[s2[i]] += 1

            # Remove the character that falls out of the window
            if i >= window_size:
                if window_count[s2[i - window_size]] == 1:
                    del window_count[s2[i - window_size]]
                else:
                    window_count[s2[i - window_size]] -= 1

            # Check if the window matches the s1 frequency
            if window_count == s1_count:
                return True

        return False
        
        