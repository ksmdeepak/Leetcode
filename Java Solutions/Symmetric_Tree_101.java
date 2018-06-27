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
     public boolean mirror(TreeNode root1, TreeNode root2) {
        if(root1 == null && root2==null)
            return true;
        else if(root1!=null && root2!=null ){
            if(root1.val==root2.val){
                return (mirror(root1.left,root2.right) && mirror(root1.right,root2.left));
            }
                
            else 
                return false;
        }
         else{
             return false;
         }
        
    }
    public boolean isSymmetric(TreeNode root) {
        return mirror(root,root);
    }
}