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
    int ans=0;
    public int findMaxPath(TreeNode root){
        if(root==null)
            return 0;
        int left = findMaxPath(root.left);
        int right = findMaxPath(root.right);
        int leftPath =0 ; int rightPath=0;
        if(root.left!=null && root.val==root.left.val)
            leftPath = left+1;
        if(root.right!=null && root.val==root.right.val)
            rightPath = right+1;
        ans = Math.max(ans,leftPath+rightPath);
        return Math.max(leftPath,rightPath);
        
    }
    public int longestUnivaluePath(TreeNode root) {
        findMaxPath(root);
        return ans;
    }
}