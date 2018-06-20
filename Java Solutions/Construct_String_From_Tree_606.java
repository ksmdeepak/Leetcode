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
    
   
    public String tree2str(TreeNode t) {
        if(t==null)
            return "";
        if(t.right==null && t.left==null)
            return t.val+"";
        else if(t.right==null)
            return t.val+"("+tree2str(t.left)+")";
        else if(t.left==null)
            return t.val+"()"+"("+tree2str(t.right)+")";
        else 
            return t.val+"("+tree2str(t.left)+")" + "("+tree2str(t.right)+")";
        
    }
}