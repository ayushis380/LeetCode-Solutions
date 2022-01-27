/* 1305. ALl Elements in Two Binary Search Trees
[Medium] */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> res = new ArrayList<>();
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        if(root1 !=null)
            helper(root1, res);
        if(root2 != null)
            helper(root2,res);
        Collections.sort(res);
        return res;
    }
  // Helper function for the InOrder Traversal
    public void helper(TreeNode root, List<Integer> res){
       if(root.left != null)
           helper(root.left, res);
       res.add(root.val);
       if(root.right != null)
           helper(root.right, res);
    }
}
