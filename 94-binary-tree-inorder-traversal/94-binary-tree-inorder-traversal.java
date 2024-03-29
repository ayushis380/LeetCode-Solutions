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
    public List<Integer> inorderTraversal(TreeNode root) {
         List<Integer> res = new ArrayList<>();
        if(root == null)
            return res;
        Stack<TreeNode> s = new Stack<>();
        while(true){
            if(root != null){
                s.push(root);
                root = root.left;
            }
            else{
                if(s.isEmpty())
                    break;
                root = s.pop();
                res.add(root.val);
                root = root.right;
            }
        }
        return res;
    }
}