\/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean identical(TreeNode root1, TreeNode root2){
        if(root1==null && root2==null)
            return true;
        else if(root1!=null && root2!=null){
            if(root1.val==root2.val)
                return identical(root1.left,root2.left) && identical(root1.right,root2.right);
            else 
                return false;
        }      
        else
            return false;
    }
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(s==null || t==null)
            return false;
        boolean result;
        if(s.val==t.val){
            result = identical(s,t);
            if(result)
                return result;
            else{
                result=isSubtree(s.left,t);
                if(result)
                    return true;
                result=isSubtree(s.right,t);
                if(result)
                    return true;
            }
        }
        else{
            
            result = isSubtree(s.left,t);
            if(result)
                    return true;
            result = isSubtree(s.right,t);
            if(result)
                    return true;
        }
        return false;
        
    }
}