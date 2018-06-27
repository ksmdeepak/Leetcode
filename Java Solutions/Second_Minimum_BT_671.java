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
    int min = Integer.MAX_VALUE;
    int min1 =  Integer.MAX_VALUE;
    public void traverse(TreeNode root){
        if(root==null)
            return ;
        if(root.val>min && root.val<min1)
            min1=root.val;
        else{
            traverse(root.left);
            traverse(root.right);
        }
      
    }
    public int findSecondMinimumValue(TreeNode root) {
        min = root.val;
        traverse(root.left);
        traverse(root.right);
        if(min1!=Integer.MAX_VALUE)
            return min1;
        else 
            return -1;
        
    }
}