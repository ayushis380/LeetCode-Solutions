# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0  # Holds the maximum length of the univalue path (in edges)

    def solve(self, root, parent_val):
        if not root:
            return 0

        # Recursively compute univalue path length for left and right subtrees
        left = self.solve(root.left, root.val)
        right = self.solve(root.right, root.val)

        # Update the answer using both sides (this is the full path through current node)
        self.ans = max(self.ans, left + right)

        # If current node matches parent's value, it can be part of univalue path
        return max(left, right) + 1 if root.val == parent_val else 0

    def longestUnivaluePath(self, root):
        self.solve(root, -1)  # Use a sentinel value as the root has no parent
        return self.ans
