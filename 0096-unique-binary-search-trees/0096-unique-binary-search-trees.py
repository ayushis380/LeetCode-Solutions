class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        # at every index i imagine i as root, where 1 to i-1 will be left subtree and i+ 1 to n is right subtree
        # i = 3, lefts = from 1, 2 and rights = 4, 5 - each gives 2 valid subtrees = 2 * 2 = 4 
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        
        print(G)
        return G[n]