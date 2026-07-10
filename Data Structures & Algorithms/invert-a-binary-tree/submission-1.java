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
    public TreeNode invertTree(TreeNode root) {
        // recursive functions for left and right nodes
        // simple varaible swap
        // OR iterative while loop swap
        TreeNode node = root;
        if (node != null) {
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;

            invertTree(node.right);
            invertTree(node.left);
        }

        return root;
    }
}
