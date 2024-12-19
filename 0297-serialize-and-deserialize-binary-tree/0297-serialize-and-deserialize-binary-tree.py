# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # preorder traversal 
        # root left right - easier to decode, as everything will come after other in order
        result = []

        def dfs(node):
            nonlocal result # needs a nonlocal as we are updating it
            if not node:
                result.append("N")
                return
            
            result += str(node.val) # if we append ',' with each val then at last val we will have ',' which creates an extra element during split
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(result)
        return ','.join(result) 
        

    def deserialize(self, data):
        ind = 0
        values = data.split(',')

        def dfs():
            nonlocal ind
            if values[ind] == "N": # nonlocal for values not required as we are only accessing it
                ind += 1
                return None
            
            # accessing according to preorder
            node = TreeNode(int(values[ind])) # access each value
            ind += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))