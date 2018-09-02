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
        if(root.val==p.val)
            return p;
        if(root.val==q.val)
            return q;
       if(p.val<q.val){
            TreeNode temp = p;
           p=q;
           q=temp;
        }
        if (root.val<p.val && root.val>q.val)
                return root;
       else{
           if(root.val>p.val)
               return lowestCommonAncestor(root.left,p,q);
           else
               return lowestCommonAncestor(root.right,p,q);
       }
    }
}