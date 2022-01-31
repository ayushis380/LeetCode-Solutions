/** 
101. Symmetric Tree
[Easy]

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
    public boolean isSymmetric(TreeNode root) {
        return check(root,root); 
    }
    public boolean check(TreeNode fNode, TreeNode sNode){
        // this function checks if the value of first and second node matches
        if(fNode ==null && sNode == null)
            return true;
        if(fNode == null || sNode == null)
            return false;
        return (fNode.val == sNode.val) && check(fNode.left,sNode.right) 
            && check(fNode.right,sNode.left);
    }
}
// Time Complexity: O(n) as we will traverse the entire input tree once and n is the total number of nodes in the tree.
// Space Complexity: O(n) as recursive calls build up the stack.
