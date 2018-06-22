/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int max=0;
    public int height (TreeNode root) {
       if(root==null)
           return 0;
        
        int l= height(root.left);
        int r=height(root.right);
        if(l+r>max)
            max=l+r;
        return Math.max(1+l,1+r);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        if(root==null)
            return 0;
        height(root);
        return max;
    }
}