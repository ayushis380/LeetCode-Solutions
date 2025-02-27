class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Sort (timestamp, username, website) triplets based on timestamp
        sorted_data = sorted(zip(timestamp, username, website))
        
        # Step 2: Create a mapping of user -> visited websites in timestamp order
        visitMap = defaultdict(list)
        for _, user, site in sorted_data:
            visitMap[user].append(site)
        
        # Step 3: Generate all 3-sequence patterns for each user
        patterns = defaultdict(int)
        for sites in visitMap.values():
            if len(sites) < 3:
                continue
            unique_patterns = set()  # Ensure each user contributes unique sequences
            
            # Generate all 3-sequences
            length = len(sites)
            for i in range(length - 2):
                for j in range(i + 1, length - 1):
                    for k in range(j + 1, length):
                        pattern = (sites[i], sites[j], sites[k])  # Store as tuple
                        unique_patterns.add(pattern)
            
            # Count unique patterns per user - score of pattern is how many users visited it
            # so if a user visits a pattern multiple times, then only it will be counted as 1 for a user
            for pattern in unique_patterns:
                patterns[pattern] += 1
        
        # Step 4: Find the most frequent pattern with lexicographically smallest order
        max_count = 0
        lex_smallest = None

        print(patterns)

        for pattern, count in patterns.items():
            if count > max_count or (count == max_count and pattern < lex_smallest):
                max_count = count
                lex_smallest = pattern

        return list(lex_smallest)

