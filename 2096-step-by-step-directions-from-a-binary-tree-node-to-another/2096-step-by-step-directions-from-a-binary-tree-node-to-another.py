# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # build the path for start and dest values - it will be same till the LCA of these nodes
        # after LCA. start and dest will be in different dir
        # so L of start if converted to U and R of dest will give us the full path
        def dfs(node, path, target):
            if not node:
                return None # false
            if node.val == target:
                return path
#      When res = None, it evaluates to False.
# When res = path (a non-empty list), it evaluates to True.
# So as long as res is not falsy, the DFS will return the path
            path.append("L")
            res = dfs(node.left, path, target)
            if res: return res

            path.pop()
            path.append("R")
            res = dfs(node.right, path, target)
            if res: return res

            path.pop() # if none of the values match then go in diffrent direction by popping all 
            return None
        
        start = dfs(root, [], startValue)
        dest = dfs(root, [], destValue)
        i = 0

        while i < min(len(start), len(dest)):
            if start[i] != dest[i]: # first non matching value
                break
            i += 1
        res = ["U"] * len(start[i:]) + dest[i:]
        return "".join(res)

