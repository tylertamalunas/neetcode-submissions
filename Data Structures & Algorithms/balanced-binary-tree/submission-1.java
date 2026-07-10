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
    public boolean isBalanced(TreeNode root) {
        // post order
        // get height and check if difference between left and right is more than 1

        
        if (height(root) == -1) return false;
        else return true;


    }
    private int height(TreeNode node) {
        if (node == null) return 0;

        int left = height(node.left);
        int right = height(node.right);
        int res = left - right;


        if (left == -1 || right == -1 || res < -1 || res > 1) return -1;
        else return 1 + Math.max(left, right);
    }
}

