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
    int sum=0;
    public int findSum(TreeNode root,boolean left) {
        if(root==null)
            return 0;
        if(root.left==null && root.right==null && left)
           sum = sum+root.val;
        findSum(root.left,true);
        findSum(root.right,false);
        return sum;
       
    }
    public int sumOfLeftLeaves(TreeNode root) {
        if(root==null)
            return 0;
        return findSum(root,false);
             
    }
}