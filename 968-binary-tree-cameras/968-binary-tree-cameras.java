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
    public int minCameraCover(TreeNode root) {
        int[] res = helper(root);
        return Math.min(res[1], res[2]);
    }
    public int[] helper(TreeNode node){
        if(node== null)
            return new int[]{0,0,99999};
        int[] L = helper(node.left);
        int[] R = helper(node.right);
        int L12 = Math.min(L[1], L[2]);
        int R12 = Math.min(R[1], R[2]);
        
        int v0= L[1] +R[1];
        int v1 = Math.min(L[2]+ R12, R[2]+ L12);
        int v2 = 1 + Math.min(L[0], L12) + Math.min(R[0], R12);
        return new int[]{v0,v1,v2};
    }
 }