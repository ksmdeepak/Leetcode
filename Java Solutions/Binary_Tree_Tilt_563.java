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
    int tilt=0;
    public int computeTilt(TreeNode root){
        if(root==null)
            return 0;
        if(root.left== null && root.right==null){
             return root.val;
        }
           
        else if(root.left==null){
            int r = computeTilt(root.right);
            tilt =tilt + Math.abs(r);
            return root.val + r;
        }
        else if(root.right==null){
            int l = computeTilt(root.left);
            tilt =tilt + Math.abs(l);
            return root.val + (l);
        }
        else{
            int l = computeTilt(root.left);
            int r = computeTilt(root.right);
            
            tilt = tilt + Math.abs(l-r);
            
            return root.val+r+l;
            
        }
    }
    public int findTilt(TreeNode root) {
        computeTilt(root);
        return tilt;
    }
}