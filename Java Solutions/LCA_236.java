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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null)
            return null;
        TreeNode a = lowestCommonAncestor(root.left,  p,  q);
        TreeNode b = lowestCommonAncestor(root.right,  p,  q); 
        if(root.val==p.val || root.val==q.val){
            return root;
        }
        else{
            
            if(a!=null && b!=null)
                return root;
            else if(a!=null)
                return a;
            else if(b!=null)
                return b;
            else
                return null;
        }
    }
}