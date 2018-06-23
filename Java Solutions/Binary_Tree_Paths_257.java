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
    List<String> output = new ArrayList<String>();
    
    public void compute(TreeNode root,String str) {
        if(root==null)
            return;
        if(root.left==null && root.right==null){
            str = str +"->"+root.val;
            output.add(str.substring(2,str.length()));
        }
            
        compute(root.left,str+"->"+root.val);
        compute(root.right,str+"->"+root.val);
        
        
    }
    
    public List<String> binaryTreePaths(TreeNode root) {
       compute(root,"");
       return output;
        
    }
}