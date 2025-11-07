# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def preorder(root):
            if not root:
                return "N"
            
            return str(root.val) + "," + preorder(root.left) + "," + preorder(root.right)
        
        return preorder(root)
        

    def deserialize(self, data):
        arr = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if arr[i] == "N":
                i += 1
                return None
            
            root = TreeNode(int(arr[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))