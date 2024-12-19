# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        data = []
        def dfs(root):
            nonlocal data

            if not root:
                data.append("N")
                return
            data.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(data)
        

    def deserialize(self, data):
        nodes = data.split(',')
        ptr = 0
        def dfs():
            nonlocal ptr
            if nodes[ptr] == "N":
                ptr += 1
                return None
            root = TreeNode(int(nodes[ptr]))
            ptr += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))