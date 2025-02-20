# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        prelist = []

        def preorder(root):
            if not root:
                prelist.append("N")
                return
            
            prelist.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)
        return ",".join(prelist)

    def deserialize(self, data):
        preorder = data.split(",")
        ind = 0

        def dfs():
            nonlocal ind
            if preorder[ind] == "N":
                ind += 1
                return None
            
            root = TreeNode(int(preorder[ind]))
            ind += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))